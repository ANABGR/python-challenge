# Import Os File
import os

# Module for read CVS file
import csv

# Set path for file
csvpath = os.path.join('..', 'Resources', 'PyPoll_Resources_election_data.csv')

# Open and read the CSV and specifies delimiter
with open(csvpath, newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',',header=0)

print("Analysis")
print("---------------------------")
    

    #variables
    khancount = 0
    khanpercent = 0
    correycount = 0
    correypercent = 0
    licount = 0
    lipercent = 0
    otooleycount = 0
    otooleypercent = 0
    winnercount = 0
    totalcount = 0
    winner = ""
    for row in csvreader:
        totalcount = totalcount + 1
        # +1 vote for Khan
        if(row[2] == "Khan"): 
            khancount = khancount + 1
        # +1 vote for Correy
        elif (row[2] == "Correy"): 
            correycount = correycount + 1
        # +1 vote for Li
        elif (row[2] == "Li"): 
            licount = licount + 1
        # +1 vote for O'Tooley
        elif (row[2] == "O'Tooley"): 
            otooleycount = otooleycount + 1
# percentage over the total
khanpercent = khancount / totalcount * 100
correypercent = correycount / totalcount * 100
lipercent = licount / totalcount * 100
otooleypercent = otooleycount / totalcount * 100
