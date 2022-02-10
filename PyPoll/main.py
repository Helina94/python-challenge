# Import Dependencies
from functools import total_ordering
import os
import csv

# Relative Path to file
csv_path = os.path.join("Resources/election_data.csv")
text_path = os.path.join("Analysis/election_results.txt")

# Initializing variables
total_votes = 0
candidate_list = []
candidate_vote = {}
candidate_winner = ""
winning_count = 0

# Open file
with open (csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Bypass the header
    csv_header = next(csvreader)
    
    for row in csvreader:

        total_votes += 1

        # Create a list of candidates
        candidate = row[2]

        # Check if candidate is in list
        if candidate not in candidate_list:
            candidate_list.append(candidate)

            # Count each candidate's vote
            candidate_vote[candidate] = 0

        # Add vote to candidate's votes
        candidate_vote[candidate] = candidate_vote[candidate] +1


# # Print to Terminal
# print(Output)
# print(candidate_vote)

# export a text file
with open (text_path, "w") as txt_file:



    # Generate Summary
    Output = (
        f"Election Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------------\n"
        

    )
    print(Output)

    #Save results to txt file
    txt_file.write(Output)


    # Determine winner
    for candidate in candidate_vote:
        # Get votes
        votes = candidate_vote.get(candidate)

        # Get vote percentage
        vote_percentage = int(votes) / total_votes * 100

        # Get the winner
        if (votes > winning_count):
            winning_count = votes
            candidate_winner = candidate

        # Print each candidate vote count and percentage
        election_results = (
             f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
        print (election_results)


        # Save txt file
        txt_file.write(election_results)

    winner = (
        f"----------------------------\n"
        f"Winner: {candidate_winner}\n"
        f"----------------------------\n")

    print(winner)
    
    # Save txt file
    txt_file.write(winner)

       

    
    
    