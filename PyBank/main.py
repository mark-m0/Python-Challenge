import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#skip the header when using any values moving forward
    header = next(csvreader)

# Count all of the lines in the file
    lines = len(list(csvreader))
    print((lines))

# Add the values of the 2nd line (profit/losses) skipping the header
