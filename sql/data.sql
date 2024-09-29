PRAGMA foreign_keys = ON;

-- insert 8 patients, a doctor and a pharmacist
INSERT INTO
    users (username, name, password, is_patient, is_doctor)
VALUES
    (
        'junkit',
        'Jun Kit',
        'sha512$e5480e0fdfc74b1f9c3032924ae1ec23$9fdb24725414842de3e3623c8a37865a9efb766edf1a50d34506ebf503788515efcd05cdefeefaf6e19717e887bc11e59ef9fa0e508782b70987ed405dee8002',
        1,
        0
    ),
    (
        'weiit',
        'Wei Jiang',
        'sha512$e5480e0fdfc74b1f9c3032924ae1ec23$9fdb24725414842de3e3623c8a37865a9efb766edf1a50d34506ebf503788515efcd05cdefeefaf6e19717e887bc11e59ef9fa0e508782b70987ed405dee8002',
        1,
        0
    ),
    (
        'ethanpoo',
        'Ethan Loo',
        'sha512$e5480e0fdfc74b1f9c3032924ae1ec23$9fdb24725414842de3e3623c8a37865a9efb766edf1a50d34506ebf503788515efcd05cdefeefaf6e19717e887bc11e59ef9fa0e508782b70987ed405dee8002',
        0,
        1
    ),
    (
        'andrea',
        'Andrea Valentino',
        'sha512$e5480e0fdfc74b1f9c3032924ae1ec23$9fdb24725414842de3e3623c8a37865a9efb766edf1a50d34506ebf503788515efcd05cdefeefaf6e19717e887bc11e59ef9fa0e508782b70987ed405dee8002',
        0,
        0
    ),
    (
        'alyssa',
        'Alyssa Estrada',
        'sha512$e5480e0fdfc74b1f9c3032924ae1ec23$9fdb24725414842de3e3623c8a37865a9efb766edf1a50d34506ebf503788515efcd05cdefeefaf6e19717e887bc11e59ef9fa0e508782b70987ed405dee8002',
        1,
        0
    ),
    (
        'gabe',
        'Gabriel Huvener',
        'sha512$e5480e0fdfc74b1f9c3032924ae1ec23$9fdb24725414842de3e3623c8a37865a9efb766edf1a50d34506ebf503788515efcd05cdefeefaf6e19717e887bc11e59ef9fa0e508782b70987ed405dee8002',
        1,
        0
    ),
    (
        'priya',
        'Priya Patel',
        'sha512$e5480e0fdfc74b1f9c3032924ae1ec23$9fdb24725414842de3e3623c8a37865a9efb766edf1a50d34506ebf503788515efcd05cdefeefaf6e19717e887bc11e59ef9fa0e508782b70987ed405dee8002',
        1,
        0
    ),
    (
        'gabec',
        'Gabriel Campos',
        'sha512$e5480e0fdfc74b1f9c3032924ae1ec23$9fdb24725414842de3e3623c8a37865a9efb766edf1a50d34506ebf503788515efcd05cdefeefaf6e19717e887bc11e59ef9fa0e508782b70987ed405dee8002',
        1,
        0
    ),
    (
        'elisa',
        'Elisa Loo',
        'sha512$e5480e0fdfc74b1f9c3032924ae1ec23$9fdb24725414842de3e3623c8a37865a9efb766edf1a50d34506ebf503788515efcd05cdefeefaf6e19717e887bc11e59ef9fa0e508782b70987ed405dee8002',
        1,
        0
    ),
    (
        'luch',
        'Luca Huvener',
        'sha512$e5480e0fdfc74b1f9c3032924ae1ec23$9fdb24725414842de3e3623c8a37865a9efb766edf1a50d34506ebf503788515efcd05cdefeefaf6e19717e887bc11e59ef9fa0e508782b70987ed405dee8002',
        1,
        0
    );

-- insert patients data
INSERT INTO
    patient (name, username, dob, age, sex, height, weight)
VALUES
    (
        'Jun Kit',
        'junkit',
        '2003-02-11 14:30:00',
        21,
        1,
        175,
        73
    ),
    (
        'Wei Jiang',
        'weiit',
        '2003-09-28 10:00:00',
        21,
        1,
        170,
        65
    ),
    (
        'Alyssa Estrada',
        'alyssa',
        '2003-02-09 10:00:00',
        21,
        1,
        170,
        50
    ),
    (
        'Gabriel Huvener',
        'gabe',
        '2003-09-28 00:00:00',
        21,
        1,
        170,
        70
    ),
    (
        'Priya Patel',
        'priya',
        '2003-09-28 10:00:00',
        21,
        1,
        165,
        50
    ),
    (
        'Gabriel Campos',
        'gabec',
        '2005-09-28 10:00:00',
        19,
        1,
        1790,
        80
    ),
    (
        'Elisa Loo',
        'elisa',
        '2003-12-09 10:00:00',
        20,
        1,
        170,
        60
    ),
    (
        'Luca Huvener',
        'luch',
        '2003-01-20 08:00:00',
        21,
        1,
        180,
        70
    );

-- insert some medicine
INSERT INTO
    medicine (name, description)
VALUES
    ('Panadol', 'Over the counter painkillers'),
    (
        'Ibuprofen',
        'Anti-inflammatory drug used for pain relief'
    ),
    (
        'Aspirin',
        'Used to reduce fever, pain, and inflammation'
    ),
    (
        'Metoprolol',
        'Beta-blocker used for high blood pressure and chest pain'
    ),
    (
        'Chlorpheniramine',
        'Antihistamine used to relieve allergy symptoms such as sneezing, runny nose, and itchy eyes'
    ),
    (
        'Acetaminophen',
        'Often used to reduce fever and treat headaches and minor aches and pains'
    );

-- insert active medicine
INSERT INTO
    active_med (
        patientid,
        name,
        dosage,
        frequency,
        quantity,
        is_flexible_duration,
        duration,
        remaining_quantity,
        last_taken,
        date_collected
    )
VALUES
    (
        1,
        'Panadol',
        2,
        3,
        12,
        0,
        4,
        12,
        '2024-09-26 22:00:00',
        '2024-09-24 10:00:00'
    ),
    (
        1,
        'Ibuprofen',
        2,
        3,
        1,
        0,
        4,
        1,
        NULL,
        '2024-09-29 00:00:00'
    ),
    (
        1,
        'Acetaminophen',
        2,
        3,
        12,
        0,
        4,
        12,
        NULL,
        NULL
    ),
    (
        1,
        'Chlorpheniramine',
        2,
        3,
        12,
        0,
        4,
        12,
        NULL,
        NULL
    ),
    (
        1,
        'Metoprolol',
        2,
        3,
        1,
        0,
        4,
        1,
        DATETIME ('now', '-479 minutes'),
        DATETIME ('now', '-1 day')
    ),
    (
        3,
        'Chlorpheniramine',
        2,
        3,
        12,
        0,
        4,
        12,
        NULL,
        NULL
    ),
    (
        2,
        'Metoprolol',
        2,
        3,
        12,
        0,
        4,
        12,
        NULL,
        '2024-09-24 10:00:00'
    );

-- insert some history for patients
INSERT INTO
    history (patientid, date, notes)
VALUES
    (
        1,
        '2024-09-24 10:00:00',
        'Sore throat and fever. Difficulty breathing at night. Prescribed xyz for 2 weeks, will monitor.'
    );

-- insert some patient logs
INSERT INTO
    logs (patientid, date, content)
VALUES
    (
        1,
        '2024-09-25 10:00:00',
        'Medicine xyz makes me feel nauseous, threw up because of it.'
    );

-- insert some states
INSERT INTO
    states (
        patientid,
        active_medicineid,
        medication,
        date,
        taken
    )
VALUES
    (1, 1, 'Panadol', '2024-09-24 10:00:00', 1),
    (1, 1, 'Panadol', '2024-09-24 18:00:00', 0),
    (1, 1, 'Panadol', '2024-09-24 22:00:00', 1),
    (1, 1, 'Panadol', '2024-09-25 10:00:00', 1),
    (1, 1, 'Panadol', '2024-09-25 18:00:00', 0),
    (1, 1, 'Panadol', '2024-09-25 22:00:00', 0),
    (1, 1, 'Panadol', '2024-09-26 10:00:00', 1),
    (1, 1, 'Panadol', '2024-09-26 18:00:00', 1),
    (1, 1, 'Panadol', '2024-09-26 22:00:00', 1),
    --
    (2, 6, 'Metoprolol', '2024-09-26 10:00:00', 1),
    (2, 6, 'Metoprolol', '2024-09-26 18:00:00', 1),
    (2, 6, 'Metoprolol', '2024-09-26 22:00:00', 1),
    (2, 6, 'Metoprolol', '2024-09-27 10:00:00', 1),
    (2, 6, 'Metoprolol', '2024-09-27 18:00:00', 0),
    (2, 6, 'Metoprolol', '2024-09-27 22:00:00', 1),
    (2, 6, 'Metoprolol', '2024-09-28 10:00:00', 1),
    (2, 6, 'Metoprolol', '2024-09-28 18:00:00', 1),
    (2, 6, 'Metoprolol', '2024-09-28 22:00:00', 1);