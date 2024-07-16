### Overview
This Python script (Main2.py) is designed to analyze election data from a CSV file (election_data.csv) and determines the election results. It performs the following tasks:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote

## Usage 

Utilized ChatGPT and Github Copilot to help with scripting. 

## Initialization:
- Sets up the path to the CSV file containing the election data.
- Initializes variables to store the total number of votes and a dictionary to count the votes for each candidate.

## CSV Processing Function:
- Defines a function `process_csv` that reads the CSV file and processes the data.
- Uses the `csv` module to read the CSV file and skips the header row.
- Iterates through each row of the CSV file, counts the total votes, and updates the vote count for each candidate.
- Calculates the percentage of votes each candidate received using a dictionary comprehension.
- Determines the winner of the election based on the popular vote.
- Prepares a formatted string of the election results.

## Generating Results:
- Calls the `process_csv` function to process the election data and generate the results.

## Output Results to File:
- Defines the file path for the output file `Results.txt`.
- Writes the election results to the `Results.txt` file.

## Read and Print Results:
- Defines a function `read_results` to check if the results file exists and print its contents. 
- Calls the `read_results` function to print the results to the terminal.

This script ensures that the election results are correctly processed, written to a file, and printed to the terminal for review.
