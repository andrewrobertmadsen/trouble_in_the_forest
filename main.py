# This is my project

#importing data from a csv into a list of dictionaries
import csv
import pprint
with open("appt_data.csv", "r") as f:
    reader = csv.DictReader(f)
    appt_data = list(reader)
    pprint.pprint(appt_data)

with open("pair_match.csv", "r") as f:
    reader = csv.DictReader(f)
    pairs = list(reader)
    pprint.pprint(pairs)
