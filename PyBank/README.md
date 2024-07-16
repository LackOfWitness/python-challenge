### Overview

(Main.py) is Python Script that analyzes the financial records of a company in (budget_data.csv) and returns

- The total number of months included in the dataset

- The net total amount of "Profit/Losses" over the entire period

- The changes in "Profit/Losses" over the entire period, and then the average of those changes

- The greatest increase in profits (date and amount) over the entire period

- The greatest decrease in profits (date and amount) over the entire period

## Usage 

Utilized ChatGPT and Github Copilot to help with scripting. 

## Import Necessary Modules:

The script starts by importing the `csv` and `os` modules, which are necessary for reading CSV files and handling file paths.

## Define Path to CSV File:

The path to the CSV file is defined using the `os.path.join()` function to ensure compatibility across different operating systems.

## Function to Read CSV and Process Data:

A function named `process_csv` is defined to read the CSV file and process the data.
Inside this function:
- The CSV file is opened in read mode using `open()`.
- A CSV reader object is created using `csv.reader()`.
- The header row is read using `next()`.
- Variables are initialized to store total months, net total, previous profit/loss, changes, greatest increase, and greatest decrease.

## Loop Through Rows in CSV File:

The function loops through each row in the CSV file.
For each row:
- The date and profit/loss values are extracted.
- The total number of months is incremented.
- The net total amount of profit/losses is calculated.
- If there is a previous profit/loss value, the change is calculated and added to the changes list.
- The greatest increase and decrease in profits are updated accordingly.
- The previous profit/loss value is updated.

## Calculate Average Change:

After processing all rows, the average change in profit/losses is calculated using the sum of the changes list divided by its length.

## Prepare Results Dictionary:

The results are stored in a dictionary with keys for total months, net total, average change, greatest increase in profits, and greatest decrease in profits.

## Process the CSV File and Print Results:

The `process_csv` function is called with the path to the CSV file.
The results are printed to the console with formatted output.

## Write Results to a Text File:

The file path for the results text file is defined.
The results are written to the text file in a formatted manner.

## Check if the File Exists and Read Results:

A function named `read_results` is defined to check if the results file exists and print its contents.
This function is called to read and print the results.
