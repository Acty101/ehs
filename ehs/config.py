"""ehs development configuration."""

import pathlib

APPLICATION_ROOT = "/"

# Secret key for encrypting cookies
SECRET_KEY = b"N\xfa\xfd}.\xd1\xa1\x95\x03E\x9e\xeem\x9ff\xcb\xdf\x18Qx\xd9\x9c\x96O"
SESSION_COOKIE_NAME = "login"

# Database file is var/ehs.sqlite3
EHS_ROOT = pathlib.Path(__file__).resolve().parent.parent
DATABASE_FILENAME = EHS_ROOT / "var" / "ehs.sqlite3"
