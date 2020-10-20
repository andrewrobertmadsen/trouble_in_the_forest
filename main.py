""" A project to test duckdb."""

import duckdb

cursor = duckdb.connect()

# Load data from csvs.
cursor.execute("CREATE TABLE appointment AS SELECT * FROM read_csv_auto('appt_data.csv');")
cursor.execute("CREATE TABLE cpt_pairs AS SELECT * FROM read_csv_auto('pair_match.csv');")

# Match on the first cpt code, write to temp table.
cursor.execute("""
    CREATE TABLE cpt_match_first AS SELECT
    patient_id
    , appointment_id
    , appointment_date
    , cpt_code
    , Pair_item1
    , Pair_item2
    , "Pair ID"
    FROM appointment INNER JOIN cpt_pairs
    ON appointment.cpt_code = cpt_pairs.Pair_item1
    ;""")

# Match second cpt code from temp table.
cursor.execute("""
    CREATE TABLE cpt_match_both AS SELECT
    a.patient_id,
    a.appointment_id,
    c."Pair ID"
    FROM appointment a INNER JOIN cpt_match_first c
    ON a.cpt_code = c.Pair_item2
    AND a.patient_id = c.patient_id
    AND a.appointment_id = c.appointment_id
    ;""")

# Write matches to csv.
cursor.execute("""
    COPY cpt_match_both
    TO 'cpt_matches.csv'
    WITH (HEADER 1, DELIMITER ',')
    ;""")
