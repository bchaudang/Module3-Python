from pathlib import Path
import csv

#set path for csv
csvpath = Path('Resources/election_data.csv')

#set variables
totalVotes = 0
candidateVotes = {}
winner = ""
maxVotes = 0

#csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header row
    csvheader = next(csvreader)

    #read each row of data after header
    for row in csvreader:
        # candidate name in the row
        candidate = row[2]

        #calculate votes for each candidate
        if candidate in candidateVotes:
            candidateVotes[candidate] += 1
        else:
            candidateVotes[candidate] = 1

        #total number of votes
        totalVotes += 1

#results output
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
for candidate, votes in candidateVotes.items():
    percentage = round((votes / totalVotes) * 100, 2)
    print(f"{candidate}: {percentage}% ({votes})")
    if votes > maxVotes:
        max_votes = votes
        winner = candidate
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")