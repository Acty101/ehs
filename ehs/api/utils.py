"""Utility functions shared by scripts."""

import uuid
import hashlib
from sqlite3 import Connection
import flask
from collections import defaultdict
from datetime import datetime, timedelta
from enum import Enum


class IdentityStatus(Enum):
    PATIENT = 0
    PHARMACIST = 1
    DOCTOR = 2


def add_patient_adherence(patient: dict, connection: Connection, x: int = None):
    """Adds the latest <x> days (or all of them) of patient adherence data to <patient>."""
    if x is not None:
        start_date = datetime.now() - timedelta(days=x)
        start_date_str = start_date.strftime("%Y-%m-%d")
        taken_medicine = connection.execute(
            """
            SELECT DATE(date) AS day, medication, taken
            FROM states
            WHERE patientid == ? 
            AND DATE(date) BETWEEN ? AND DATE('now', 'localtime')
            ORDER BY date DESC
            """,
            (patient["patientid"], start_date_str),
        )
    else:
        taken_medicine = connection.execute(
            """
            SELECT DATE(date) AS day, medication, taken
            FROM states
            WHERE patientid == ? 
            ORDER BY date DESC
            """,
            (patient["patientid"],),
        )
    taken_medicine = taken_medicine.fetchall()
    medicines = defaultdict(lambda: {"date": "", "content": []})
    for taken in taken_medicine:
        day = taken["day"]
        medicines[day]["date"] = day
        medicines[day]["content"].append(
            {"medication": taken["medication"], "taken": bool(taken["taken"])}
        )
    patient["adherence"] = list(medicines.values())


def logged_in():
    """Return true if user is logged in."""
    return "username" in flask.session


def is_doctor(connection: Connection) -> bool:
    """Return true if current flask session username is a doctor"""
    if not logged_in():
        return False
    username = flask.session["username"]
    status = connection.execute(
        "SELECT is_doctor FROM users WHERE username == ?", (username,)
    )
    return status.fetchone()["is_doctor"] == 1


def create_salt_hashed_password(password: str) -> str:
    """Create hashed password with random salt for a new user."""
    algorithm = "sha512"
    salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + password
    hash_obj.update(password_salted.encode("utf-8"))
    password_hash = hash_obj.hexdigest()
    return "$".join([algorithm, salt, password_hash])


def salt_and_hash_password(salt: str, password: str) -> str:
    """Return a hashed password using the given salt."""
    algorithm = "sha512"
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + password
    hash_obj.update(password_salted.encode("utf-8"))
    password_hash = hash_obj.hexdigest()
    return "$".join([algorithm, salt, password_hash])


def get_salt(connection: Connection, username: str) -> str:
    """Return the salt value of a given use."""
    pw = connection.execute(
        "SELECT password FROM users WHERE username == ?", (username,)
    )
    pw = pw.fetchone()
    pw = pw["password"].split("$")[1] if pw is not None else ""
    return pw
