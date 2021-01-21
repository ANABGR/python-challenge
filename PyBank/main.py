# Import Os File
import os

# Module for read CVS file
import csv

# Set path for file
csvpath = os.path.join('..', 'Resources', 'PyBank_Resources_budget_data.csv')

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


# The total number of months included in the dataset
