import os
import csv


csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    votes = len(list(csvreader))

    


    print("Election Results:")
    print("-----------------------------")
    print(f"Total Votes: {votes}")
    #print(f"Total: {total}")
    #print(f"Average Change: {avgChange}")
    #print(f"Greatest Increase in Profits: {greatIncr}")
    #print(f"Greatest Decrease in Profits: {greatDecr}")
