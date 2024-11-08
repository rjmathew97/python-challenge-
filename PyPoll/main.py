import os
import csv

csv_path_load = os.path.join("Resources", "election_data.csv")
csv_path_output = os.path.join("analysis", "election_analysis.txt")

# Initialize variables
total_votes = 0
candidate_votes = {}

# Open and read the csv
with open(csv_path_load) as file:
    reader = csv.reader(file)

    # Skip the header row
    header = next(reader)
    
    # Loop through each row in the CSV
    for row in reader:
    # Collect the number of vote 
        total_votes += 1
        candidate = row[2]

#Add vote to the candidate's count 
        if candidate in candidate_votes: 
            candidate_votes [candidate] += 1 
        else:
            candidate_votes [candidate] = 1

candidate_percentages = {}
for candidate, votes in candidate_votes.items():
    candidate_percentages [candidate] = (votes / total_votes) * 100

winner = max(candidate_votes, key=candidate_votes.get)

# Print the output
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")

for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages [candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("----------------------------")    
print(f"Winner: {winner}")
print("----------------------------")  