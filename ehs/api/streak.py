"""Streak related API."""

import ehs
from flask import Response


@ehs.app.route("/api/v1/up_streak/<int:id>/", methods=["POST"])
def incr_streak(id):
    """Increment streak."""
    connection = ehs.model.get_db()
    connection.execute(
        "UPDATE patient SET streak = streak + 1 WHERE patientid == ?", (id,)
    )
    return Response(status=200)


@ehs.app.route("/api/v1/reset_streak/<int:id>", methods=["POST"])
def reset_streak(id):
    """Reset streak to 0."""
    connection = ehs.model.get_db()
    connection.execute("UPDATE patient SET streak = 0 WHERE patientid == ?", (id,))
    return Response(status=200)
