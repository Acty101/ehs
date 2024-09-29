"""Patient related API."""

import ehs
import flask
from ehs.api.utils import *
import uuid

import ehs.model


@ehs.app.route("/api/v1/patients/", methods=["GET"])
def get_patients():
    """Get a list of all patients and a small summary of them."""
    connection = ehs.model.get_db()
    # if not is_doctor(connection):
    #     flask.abort(401)
    patients = connection.execute("SELECT patientid, name, dob, sex FROM patient")
    patients = patients.fetchall()
    # find latest 3 medicine states
    for patient in patients:
        add_patient_adherence(patient, connection, 5)
        patient["sex"] = "male" if patient["sex"] == 1 else "female"
    return flask.jsonify(patients), 200


@ehs.app.route("/api/v1/patient/<int:id>/", methods=["GET"])
def get_patient(id: int):
    """Get the full details of a single patient."""
    # if not is_doctor(connection):
    #     flask.abort(401)
    connection = ehs.model.get_db()
    patient = connection.execute("SELECT * FROM patient WHERE patientid == ?", (id,))
    patient = patient.fetchone()
    patient["sex"] = "male" if patient["sex"] == 1 else "female"
    return flask.jsonify(patient), 200


@ehs.app.route("/api/v1/adherence/<int:id>")
def get_adherence(id: int):
    patient = {"patientid": id}
    connection = ehs.model.get_db()
    add_patient_adherence(patient, connection, 35)
    return flask.jsonify(patient), 200


@ehs.app.route("/api/v1/patient/", methods=["POST"])
def add_patient():
    """Add details of a patient to database and create an account for them."""

    # if not is_doctor(connection):
    #     flask.abort(401)
    username = flask.request.form.get("username")
    name = flask.request.form.get("name")
    connection = ehs.model.get_db()
    valid = connection.execute(
        "SELECT username FROM users WHERE username == ?", (username,)
    )
    valid = valid.fetchall()
    password = ""
    if len(valid) == 0:
        # need to create new user first
        password = uuid.uuid4()
        salted_pw = create_salt_hashed_password(password)
        connection.execute(
            """INSERT INTO users (username, name, password, is_patient, is_doctor)
                           VALUES (?, ?, ?, ?, ?)
                           """,
            (username, name, salted_pw, 1, 0),
        )
        message = "new account created"

    dob = flask.request.form.get("dob")
    age = flask.request.form.get("age")
    sex = flask.request.form.get("sex")
    height = flask.request.form.get("height")
    weight = flask.request.form.get("weight")
    connection.execute(
        "INSERT INTO patient (name, dob, age, sex, height, weight) VALUES (?, ?, ?, ?, ?, ?)",
        (name, dob, age, sex, height, weight),
    )
    return flask.jsonify({"message": message, "password": password}), 200


@ehs.app.route("/api/v1/log_feelings/<int:patientid>/", methods=["POST"])
def log_feelings(patientid: int):
    "Log the patient's feelings."
    content = flask.request.get_json()["content"]
    connection = ehs.model.get_db()
    connection.execute(
        """INSERT INTO logs (patientid, date, content)
                       VALUES (?, DATETIME('now'), ?)""",
        (patientid, content),
    )
    return flask.Response(status=200)


@ehs.app.route("/api/v1/get_logs/<int:patientid>/", methods=["GET"])
def get_logs(patientid: int):
    """Return logs of <patientid>."""
    connection = ehs.model.get_db()
    result = connection.execute("SELECT * FROM logs WHERE patientid == ?", (patientid,))
    result = result.fetchall()
    return flask.jsonify(result), 200


@ehs.app.route("/api/v1/search_patients/", methods=["GET"])
def search_patients():
    """Return a list of patients that contain str."""
    search_term = flask.request.args.get("name", None)
    if search_term is None:
        return flask.abort(404)
    connection = ehs.model.get_db()
    result = connection.execute(
        """SELECT patientid, name, dob, sex FROM patient 
           WHERE name LIKE ?""",
        ("%" + search_term + "%",),
    )
    result = result.fetchall()
    for patient in result:
        patient["sex"] = "male" if patient["sex"] == 1 else "female"
    return flask.jsonify(result), 200
