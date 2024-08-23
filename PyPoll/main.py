# This will allow us to create file path across operating systems
import os

# Module for reading CSV files
import csv

from collections import defaultdict

# Initialize variables for all of the calulated totals
total_votes = 0

# Store the unique names of candidates
candidates = set()

# Count the number of votes for each candidate
vote_counts = defaultdict(int)

# The 'Resources' directory containing the 'election_data.csv' records that is being analyzed
csvpath = os.path.join('Resources', 'election_data.csv')

# The 'analysis' directory containing the output of the analysis to a 'results.txt' text file
txtpath = os.path.join('analysis', 'results.txt')

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies the comma delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Read the header row first and outputs header names to Terminal
    csv_header = next(csv_reader)
    
    # Setting the ballot column as column 1 and the candidate column as column 3 
    ballot_index = 0
    candidate_index = 2

    # Read each row of data after the header and outputs content to Terminal
    for row in csv_reader:
        
        # Keep track of the total number of votes
        total_votes += 1

        # Get the candidate name from each row and adds their name to the list
        candidate_name = row[candidate_index]
        candidates.add(candidate_name)
        
        # Keep track of the total number of vote counts for the candidate
        vote_counts[candidate_name] += 1

# Print the analysis to the terminal window
print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')

# Converts the set of unique candidate names to a list
unique_candidates_list = list(candidates) 

# Goes through each candidate and their vote counts and calculates the percentage of votes for each
for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) * 100   
    print(f'{candidate}: {percentage:.3f}% ({votes})')

# The winner is the candidate with the highest number of votes
winner = max(vote_counts, key=vote_counts.get)

print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')

# Output the analysis to a text file named 'results.txt" in the 'analysis' directory, similar concept as above
with open(txtpath, 'w') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"-------------------------\n")
    for candidate, votes in vote_counts.items():
        percentage = (votes / total_votes) * 100 
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"-------------------------\n")
