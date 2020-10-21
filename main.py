# This is my project

#importing data from a csv into a list of dictionaries
import pprint
import pandas as pd


'''
with open("appt_data.csv", "r") as f:
    reader = csv.DictReader(f)
    appt_data = list(reader)
    pprint.pprint(appt_data)

with open("pair_match.csv", "r") as f:
    reader = csv.DictReader(f)
    pairs = list(reader)
    pprint.pprint(pairs)
'''
#Homework Item 1
'''
This is how I am importing the csv file.
'''
df = pd.read_csv("appt_data.csv")
print(df.head(3))

var_pair1 = 971
is_pair1 = df['cpt_code'] == var_pair1
print(is_pair1.head())

#Homework item 4
'''this code creates a unique list of cpt codes'''
cpt_list = df.cpt_code.unique()
print(cpt_list)

#Homework item 5
'''
This code creates a compound id
'''
cmpd_id = df["patient_id"] + df["appointment_id"]
print(cmpd_id)

