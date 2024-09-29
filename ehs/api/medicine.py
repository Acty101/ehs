"""Medicine related API."""

import ehs
import flask


@ehs.app.route("/api/v1/all_medicines/", methods=["GET"])
def get_all_medicine():
    connection = ehs.model.get_db()
    meds = connection.execute("SELECT * FROM medicine")
    meds = meds.fetchall()
    return flask.jsonify(meds), 200


@ehs.app.route("/api/v1/patient_meds/<int:patientid>/", methods=["GET"])
def get_patient_meds(patientid):
    """Get a list of medication that patient <id> is on."""
    connection = ehs.model.get_db()
    active_med = connection.execute(
        """
        SELECT * 
        FROM active_med
        INNER JOIN medicine ON active_med.name = medicine.name
        WHERE active_med.patientid = ? 
        AND active_med.remaining_quantity != 0
        """,
        (patientid,),
    )
    active_med = active_med.fetchall()
    return flask.jsonify(active_med), 200


@ehs.app.route("/api/v1/prescribe/<int:patientid>/", methods=["POST"])
def prescribe_meds(patientid):
    """Prescribe a medication, creates an entry in active_med."""
    med_name = flask.request.form.get("name")
    dosage = flask.request.form.get("dosage")
    frequency = flask.request.form.get("frequency")
    quantity = flask.request.form.get("quantity")
    is_flexible_duration = flask.request.form.get("is_flexible_duration")
    duration = flask.request.form.get("duration")
    required_fields = {
        "name": med_name,
        "dosage": dosage,
        "frequency": frequency,
        "quantity": quantity,
        "is_flexible_duration": is_flexible_duration,
        "duration": duration,
    }

    for field, value in required_fields.items():
        if not value:
            return flask.jsonify({"error": f"{field} is required"}), 400
    connection = ehs.model.get_db()
    connection.execute(
        """
        INSERT INTO active_med (patientid, name, dosage, frequency, quantity, is_flexible_duration, duration, remaining_quantity) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            patientid,
            med_name,
            dosage,
            frequency,
            quantity,
            1 if is_flexible_duration else 0,
            duration,
            quantity,
        ),
    )
    return flask.Response(status=200)


@ehs.app.route("/api/v1/pickup_meds/<int:active_med_id>/", methods=["POST"])
def pickup_meds(active_med_id: int):
    """Handle when a medication has been picked up."""
    connection = ehs.model.get_db()
    connection.execute(
        "UPDATE active_med SET date_collected = DATETIME('now') WHERE activeid == ?",
        (active_med_id,),
    )
    return flask.Response(status=200)


@ehs.app.route("/api/v1/take_medicine/<int:patientid>/", methods=["POST"])
def take_medicine(patientid: int):
    """Handle when a medicine is taken or not."""
    data = flask.request.get_json()
    date = data.get("date", "")
    name = data.get("name")
    med_id = data.get("id", None)
    if med_id is None:
        flask.abort(404)
    connection = ehs.model.get_db()
    taken = True
    if not date:
        # medicine was not taken
        date = None
        taken = False
    else:
        # medicine was taken, update the active meds
        connection.execute(
            """UPDATE active_med 
            SET remaining_quantity = remaining_quantity - 1,
            last_taken = DATETIME('now')
            WHERE activeid == ?""",
            (med_id,),
        )
    # put entry in the states table
    connection.execute(
        """INSERT INTO states (patientid, active_medicineid, medication, date, taken) 
                           VALUES (?, ?, ?, ?, ?)""",
        (patientid, med_id, name, date, taken),
    )
    return flask.Response(status=200)


@ehs.app.route("/api/v1/clear_medicine/<int:med_id>", methods=["DELTE"])
def clear_meds(med_id):
    """Remove active medication."""
    connection = ehs.model.get_db()
    connection.execute("DELETE FROM active_med WHERE activeid == ?", (med_id,))
    return flask.Response(status=204)
