"""History related API."""

import ehs
import flask


@ehs.app.route("/api/v1/history/<int:patientid>", methods=["GET"])
def get_patient_history(patientid):
    """Return a list of patient's history separated by dates."""
    connection = ehs.model.get_db()
    history = connection.execute(
        "SELECT * FROM history WHERE patientid == ? ", (patientid,)
    )
    history = history.fetchall()
    return flask.jsonify(history), 200
