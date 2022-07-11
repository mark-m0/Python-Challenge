import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
#skip the header when using any values moving forward
    for row in csvreader:
# Count all of the lines in the file
        total = 0
        lines = len(list(csvreader))
        total = row[1]
# Add the values of the 2nd line (profit/losses) skipping the header
    
# Print out the financial analysis
    print("Financial Analysis:")
    print("-----------------------------")
    print(f"Total Months: {lines}")
    print(f"Total: {total}")
    #print(f"Average Change: {avgChange}")
    #print(f"Greatest Increase in Profits: {greatIncr}")
    #print(f"Greatest Decrease in Profits: {greatDecr}")