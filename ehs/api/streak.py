"""Streak related API."""

import ehs
from flask import Response, request, jsonify
from datetime import datetime


@ehs.app.route("/api/v1/up_streak/<int:id>/", methods=["POST"])
def incr_streak(id):
    """Increment streak."""
    connection = ehs.model.get_db()
    connection.execute(
        "UPDATE patient SET streak = streak + 1 WHERE patientid == ?", (id,)
    )
    return Response(status=200)


@ehs.app.route("/api/v1/set_streak/<int:id>/", methods=["POST"])
def set_streak(id):
    """Set streak."""
    new_streak = request.args.get("streak")
    connection = ehs.model.get_db()
    connection.execute(
        "UPDATE patient SET streak = ? WHERE patientid == ?", (new_streak, id)
    )
    return Response(status=200)


@ehs.app.route("/api/v1/reset_streak/<int:id>", methods=["POST"])
def reset_streak(id):
    """Reset streak to 0."""
    connection = ehs.model.get_db()
    connection.execute("UPDATE patient SET streak = 0 WHERE patientid == ?", (id,))
    return Response(status=200)


@ehs.app.route("/api/v1/check_streak/<int:id>/", methods=["GET"])
def check_streak(id):
    """Return true if date given has no miss medicines."""
    date_str = request.args.get("date")
    date = datetime.strptime(date_str, "%Y-%m-%d")
    connection = ehs.model.get_db()
    res = connection.execute(
        "SELECT taken FROM states WHERE patientid = ? AND DATE(date) = ?", (id, date)
    )
    res = res.fetchall()
    if not res:
        return jsonify({"result": False}), 200
    print(res)
    for r in res:
        if not r["taken"]:
            return jsonify({"result": False}), 200
    return jsonify({"result": True}), 200


@ehs.app.route("/api/v1/streak_data/<int:id>/", methods=["GET"])
def get_streak_data(id):
    """Return ."""
    date_str = request.args.get("date")
    date = datetime.strptime(date_str, "%Y-%m-%d")
    connection = ehs.model.get_db()
    res = connection.execute(
        "SELECT taken FROM states WHERE patientid = ? AND DATE(date) = ?", (id, date)
    )
    res = res.fetchall()
    if not res:
        return jsonify({"result": False}), 200
    print(res)
    for r in res:
        if not r["taken"]:
            return jsonify({"result": False}), 200
    return jsonify({"result": True}), 200
