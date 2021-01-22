# Import Os File
import os

# Module for read CVS file
import csv

# Set path for file
csvpath = os.path.join('..', 'Resources', 'PyBank_Resources_budget_data.csv')

# Open and read the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter="," ,header=0)
    print (csvreader)


# Read rows
for row in csvreader:
        print(row)
# Variables
Months = 0
Profits = []
Dates = []

# The total number of months included in the dataset
for row in csvreader:
        Months += 1
        Dates.append(row[0])
        Profits.append(float(row[1]))

TotalProfits = Profits[0]
TotaledChanges = 0
BigInc = 0
BigDec = 0

#Calculate the change in profit
for n in range (1, Months):

total += int(row[1])
    
    
    #Check the biggest increase
    if CurrentChange > BigInc:
        BigInc = CurrentChange
        BigIncDate = Dates[n]
    elif CurrentChange < BigDec:
        BigDec = CurrentChange
        BigDecDate = Dates[n]

#Print the final results
print("Financial Analysis")
print("----------------------------")
print(f"Months: {Months}")
print(f"Total Profits: ${(TotalProfits):.2f}")
print(f"Average Change: ${(TotaledChanges/(Months - 1)):.2f}")
print(f"Greatest Increase in Profits: {BigIncDate} (${(BigInc):.2f})")
print(f"Greatest Decrease in Profits: {BigDecDate} (${(BigDec):.2f})")

#Output final results to txt file
with open("Results.txt","w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Months: {Months}\n")
    txtfile.write(f"Total Profits: ${(TotalProfits):.2f}\n")
    txtfile.write(f"Average Change: ${(TotaledChanges/(Months - 1)):.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {BigIncDate} (${(BigInc):.2f})\n")
    txtfile.write(f"Greatest Decrease in Profits: {BigDecDate} (${(BigDec):.2f})\n")