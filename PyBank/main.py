import os
import csv

file_to_load = os.path.join("Resources", "budget_data.csv")

with open(file_to_load) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
#skip the header when using any values moving forward
    header = next(reader)
    total = 0
    lines = 0
    avgChange = 0
    greatIncr = 0
    greatDecr = 0
# Add the values of the 2nd line (profit/losses) skipping the header
    for row in reader:
        total = total + int(row[1])
        lines += 1

# Print out the financial analysis
    print("Financial Analysis:")
    print("-----------------------------")
    print(f"Total Months: {lines}")
    print(f"Total: {total}")
    print(f"Average Change: {avgChange}")
    print(f"Greatest Increase in Profits: {greatIncr}")
    print(f"Greatest Decrease in Profits: {greatDecr}")