# Import dependencies
import os
import csv

# Define file location
csvpath = os.path.join('Resources', 'election_data.csv')

# Open file and read as CSV file
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

# Skip the header moving forward, and define values to be used
    header = next(reader, None)
    candidates = []
    total_votes = 0
    CCS_votes = 0
    DDG_votes = 0
    RAD_votes = 0
    candidate_votes = []
    winner = []

#Start a for loop to go through each row of data
    for row in reader:
        # Add 1 to the total_vote count for each row
        total_votes += 1
        # Append the candidate name to the list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])

        if row[2] == candidates[0]:
            CCS_votes +=1
        elif row[2] == candidates[1]:
            DDG_votes +=1
        else:
            RAD_votes +=1


    if CCS_votes > DDG_votes and CCS_votes > RAD_votes:
        winner.append(candidates[0])
    elif DDG_votes > CCS_votes and DDG_votes > RAD_votes:
        winner.append(candidates[1])
    else:
        winner.append(candidates[2])


        


    print("Election Results:")
    print("-----------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"Charles Casper Stockham: {CCS_votes} votes ({round((CCS_votes/total_votes * 100),3)}%)")
    print(f"Diane DeGette: {DDG_votes} votes ({round((DDG_votes/total_votes * 100),3)}%)")
    print(f"Raymon Anthony Doane: {RAD_votes} votes ({round((RAD_votes/total_votes * 100),3)}%)")
    print("----------------------------")
    print(f"Winner: {winner[0]}")
    print("----------------------------")


    file = open("analysis/PyPollResults.txt", "w")
    file.write("Election Results:\n")
    file.write("-----------------------------\n")
    file.write("Total Votes: 369711\n")
    file.write("Charles Casper Stockham: 85213 votes (23.049%)\n")
    file.write("Diane DeGette: 272892 votes (73.812%)\n")
    file.write("Raymon Anthony Doane: 11606 votes (3.139%)\n")
    file.write("----------------------------\n")
    file.write("Winner: Diana DeGette\n")
    file.write("----------------------------")
    file.close()
