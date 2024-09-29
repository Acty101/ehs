PRAGMA foreign_keys = ON;

CREATE TABLE
    users (
        username VARCHAR(20) PRIMARY KEY,
        name VARCHAR(40) NOT NULL,
        password VARCHAR(256) NOT NULL,
        is_patient INTEGER NOT NULL,
        is_doctor INTEGER NOT NULL,
        created DATETIME DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE
    patient (
        patientid INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(20) NOT NULL,
        name VARCHAR(40) NOT NULL,
        dob DATETIME NOT NULL,
        age INTEGER NOT NULL,
        sex INTEGER NOT NULL, -- 0 for female
        height REAL NOT NULL,
        weight REAL NOT NULL,
        streak INTEGER DEFAULT 0,
        FOREIGN KEY (username) REFERENCES users (username) ON DELETE CASCADE
    );

CREATE TABLE
    medicine (
        name VARCHAR(40) PRIMARY KEY,
        description VARCHAR(256) NOT NULL
    );

CREATE TABLE
    active_med (
        activeid INTEGER PRIMARY KEY AUTOINCREMENT,
        patientid INTEGER NOT NULL,
        name VARCHAR(40) NOT NULL,
        dosage REAL NOT NULL,
        frequency INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        is_flexible_duration INTEGER NOT NULL,
        duration REAL,
        remaining_quantity INTEGER,
        last_taken DATETIME,
        date_collected DATETIME,
        FOREIGN KEY (patientid) REFERENCES patient (patientid) ON DELETE CASCADE,
        FOREIGN KEY (name) REFERENCES medicine (name) ON DELETE CASCADE
    );

CREATE TABLE
    history (
        historyid INTEGER PRIMARY KEY AUTOINCREMENT,
        patientid INTEGER NOT NULL,
        date DATETIME NOT NULL,
        notes VARCHAR(256) NOT NULL,
        FOREIGN KEY (patientid) REFERENCES patient (patientid) ON DELETE CASCADE
    );

CREATE TABLE
    logs (
        logsid INTEGER PRIMARY KEY AUTOINCREMENT,
        patientid INTEGER NOT NULL,
        date DATETIME NOT NULL,
        content VARCHAR(256),
        FOREIGN KEY (patientid) REFERENCES patient (patientid) ON DELETE CASCADE
    );

CREATE TABLE
    states (
        statesid INTEGER PRIMARY KEY AUTOINCREMENT,
        patientid INTEGER NOT NULL,
        active_medicineid INTEGER NOT NULL,
        medication VARCHAR(40) NOT NULL,
        date DATETIME,
        taken INTEGER NOT NULL,
        FOREIGN KEY (patientid) REFERENCES patient (patientid) ON DELETE CASCADE,
        FOREIGN KEY (active_medicineid) REFERENCES active_med (activeid) ON DELETE CASCADE,
        FOREIGN KEY (medication) REFERENCES medicine (name) ON DELETE CASCADE
    );

CREATE TABLE
    blacklist (token VARCHAR(256) PRIMARY KEY)