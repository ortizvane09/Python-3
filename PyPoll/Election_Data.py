import csv
import os
election_csv = os.path.join('Resources', 'election_data.csv')
Total_Votes = 0
Candidate_Votes = {}
Candidates = []

with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    next(csvreader)

    for row in csvreader:
        Total_Votes += 1
        Candidate = row[2]

        if Candidate not in Candidates:
            Candidates.append(Candidate)
            Candidate_Votes[Candidate] = 1
        else:
            Candidate_Votes[Candidate] += 1

Winner = ""
Max_Votes = 0

print("Election results")
print("--------------------------------")
print(f"Total Votes: {Total_Votes}")
print("--------------------------------")

for Candidate in Candidates:
    Votes = Candidate_Votes[Candidate]
    Percentage = (Votes / Total_Votes) * 100
    print(f"{Candidate}: {Percentage:.3f}% ({Votes})")

    if Votes > Max_Votes:
        Max_Votes = Votes
        Winner = Candidate

print("------------------------------------------------")

print(f"Winner: {Winner}")
print("------------------------------------------------")