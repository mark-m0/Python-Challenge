#Import dependencies
import os
import csv

#Define file location
file_to_load = os.path.join("Resources", "budget_data.csv")

#Open and read file as CSV file
with open(file_to_load) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
#skip the header when using any values moving forward and define all values
    header = next(reader)
    total = 0
    lines = 0
    avgChange = 0
    initial_value = 0
    final_value = 0
    greatIncr = 0
    greatDecr = 0
    changes = []
    dates = []
    

#Calculate values
    for row in reader:
        lines += 1
        total = total + int(row[1])
        final_value = int(row[1])    
        avgChange = (final_value - initial_value)
        changes.append(avgChange)
        dates.append(row[0])
        initial_value = final_value 


    dates.append(changes)
    avgChange = sum(changes)
    greatIncr = max(changes)
    date_great = changes.index(greatIncr)
    greatDecr = min(changes)
    date_small = changes.index(greatDecr)
    

# Print out the financial analysis
    print("Financial Analysis:")
    print("-----------------------------")
    print(f"Total Months: {lines}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avgChange/lines}")
    print(f"Greatest Increase in Profits:{dates[date_great]}   ${greatIncr}")
    print(f"Greatest Decrease in Profits:{dates[date_small]}   ${greatDecr}")