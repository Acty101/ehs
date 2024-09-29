"""EHS REST API."""

from flask import jsonify
import ehs
from ehs.api.patient import *
from ehs.api.login import *
from ehs.api.medicine import *
from ehs.api.history import *
from ehs.api.streak import *


@ehs.app.route("/api/v1/")
def get_api():
    """Return list of services available."""
    context = {
        "routes": ["/api/v1/patients/", "/api/v1/patient/<int:id>/", "/api/v1/patient/"]
    }
    return jsonify(**context)
