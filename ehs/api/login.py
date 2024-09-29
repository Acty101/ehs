"""login API."""

import ehs
import flask
from ehs.api.utils import *
import ehs.model


@ehs.app.route("/api/v1/login/", methods=["POST"])
def login():
    """Login to account."""
    username = flask.request.form.get("username")
    password = flask.request.form.get("password")
    if not username or not password:
        flask.abort(400)
    # check if username and password exists in DB
    connection = ehs.model.get_db()
    is_valid_password = connection.execute(
        "SELECT EXISTS (SELECT 1 FROM users WHERE username == ? AND password == ?)",
        (
            username,
            salt_and_hash_password(get_salt(connection, username), password),
        ),
    )
    is_valid_password = list(is_valid_password.fetchone().values())[0]
    if not is_valid_password:
        flask.abort(403)
    # log user in with session obj
    flask.session["username"] = username

    res = connection.execute(
        "SELECT is_doctor FROM users WHERE username == ?", (username,)
    )
    res = res.fetchone()
    flask.session["is_doctor"] = res["is_doctor"] == 1
    return (
        flask.jsonify(
            {"message": "Login successful", "is_doctor": flask.session["is_doctor"]}
        ),
        200,
    )


@ehs.app.route("/api/v1/check_login/", methods=["GET"])
def is_logged():
    """Return true if logged in."""
    return (
        flask.jsonify(
            {
                "is_logged_in": logged_in(),
                "is_doctor": flask.session.get("is_doctor", False),
            }
        ),
        200,
    )


@ehs.app.route("/api/v1/logout/", methods=["GET"])
def logout():
    """Remove session object."""
    flask.session.clear()
    return flask.jsonify({"message": "logged out"}), 200
