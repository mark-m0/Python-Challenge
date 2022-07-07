import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#count all of the lines in the file, then subtract 1 for the header
    lines = len(list(csvreader))
    print((lines-1))

