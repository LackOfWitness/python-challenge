import csv
import os

# Define the path to the CSV file
PyBankcsv = os.path.join('Resources', 'budget_data.csv')

# Function to read CSV and process data
def process_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

        total_months = 0
        net_total = 0
        previous_profit_loss = None
        changes = []
        greatest_increase = ("", float('-inf'))
        greatest_decrease = ("", float('inf'))

        for row in csv_reader:
            date, profit_loss = row
            profit_loss = int(profit_loss)

            # Calculate the total number of months
            total_months += 1

            # Calculate the net total amount of "Profit/Losses"
            net_total += profit_loss

            # Calculate changes and keep track of the greatest increase/decrease
            if previous_profit_loss is not None:
                change = profit_loss - previous_profit_loss
                changes.append(change)

                if change > greatest_increase[1]:
                    greatest_increase = (date, change)
                
                if change < greatest_decrease[1]:
                    greatest_decrease = (date, change)

            previous_profit_loss = profit_loss

        # Calculate the average change
        average_change = sum(changes) / len(changes) if changes else 0

        # Prepare the results
        results = {
            "Total Months": total_months,
            "Net Total": net_total,
            "Average Change": average_change,
            "Greatest Increase in Profits": greatest_increase,
            "Greatest Decrease in Profits": greatest_decrease
        }

        return results

# Process the CSV file
results = process_csv(PyBankcsv)

# Print the results with blank rows between them
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {results['Total Months']}\n")
print(f"Total: ${results['Net Total']}\n")
print(f"Average Change: ${results['Average Change']:.2f}\n")
print(f"Greatest Increase in Profits: {results['Greatest Increase in Profits'][0]} (${results['Greatest Increase in Profits'][1]:.2f})\n")
print(f"Greatest Decrease in Profits: {results['Greatest Decrease in Profits'][0]} (${results['Greatest Decrease in Profits'][1]:.2f})\n")

# Define the file path for the Results.txt output
output_file_path = os.path.join("Analysis", "Results.txt")

# Open the file in write mode
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
with open(output_file_path, "w") as file:
    # Write the results to the file
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {results['Total Months']}\n")
    file.write(f"Total: ${results['Net Total']}\n")
    file.write(f"Average Change: ${results['Average Change']:.2f}\n")
    file.write(f"Greatest Increase in Profits: {results['Greatest Increase in Profits'][0]} (${results['Greatest Increase in Profits'][1]:.2f})\n")
    file.write(f"Greatest Decrease in Profits: {results['Greatest Decrease in Profits'][0]} (${results['Greatest Decrease in Profits'][1]:.2f})\n")

# Print a message indicating the file has been created
print(f"Results have been written to {output_file_path}")

# Function to check if the file_path exists to read and print out the results of this file
def read_results(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            print(file.read())
    else:
        print(f"File not found: {file_path}")


