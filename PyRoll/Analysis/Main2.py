import csv
import os

PyRollcsv = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates_votes = {}

# Function to read CSV and process data
def process_csv(file_path):
    global total_votes, candidates_votes
    
    # Read the CSV file
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header

        for row in csv_reader:
            total_votes += 1
            candidate = row[2]

            if candidate in candidates_votes:
                candidates_votes[candidate] += 1
            else:
                candidates_votes[candidate] = 1

    # Calculate the percentage of votes each candidate won using a dictionary comprehension
    candidates_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates_votes.items()}

    # Determine the winner based on popular vote
    winner = max(candidates_votes, key=candidates_votes.get)

    # Prepare the results
    results = (
        "Election Results\n\n"
        "-------------------------\n\n"
        f"Total Votes: {total_votes}\n"
        "-------------------------\n\n"
    )

    for candidate, votes in candidates_votes.items():
        percentage = candidates_percentages[candidate]
        results += f"{candidate}: {percentage:.3f}% ({votes})\n\n"

    results += (
        "-------------------------\n\n"
        f"Winner: {winner}\n\n"
        "-------------------------\n"
    )

    return results

results = process_csv(PyRollcsv)

# Define the file path for the Results.txt output
output_file_path = os.path.join("Analysis", "Results.txt")

# Write the results to the file
with open(output_file_path, 'w') as file:
    file.write(results)

# Function to check if the file_path exists to read and print out the results of this file
def read_results(output_file_path):
    if os.path.exists(output_file_path):
        with open(output_file_path, "r") as file:
            print(file.read())
    else:
        print(f"File not found: {output_file_path}")

print(results) # Print the results
