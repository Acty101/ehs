"""EHS package initializer."""

import flask
from flask_cors import CORS


app = flask.Flask(__name__)
CORS(app, supports_credentials=True)

# Read settings from config module (ehs/config.py)
app.config.from_object("ehs.config")

# In case in the future if want to secure this
app.config.from_envvar("EHS_SETTINGS", silent=True)

import ehs.api
