import os
import csv

csv_path_load = os.path.join("Resources", "budget_data.csv")
csv_path_output = os.path.join("analysis", "budget_analysis.txt")

# Initialize variables
months = []
profit_losses = []

# Open and read the csv
with open(csv_path_load) as file:
    reader = csv.reader(file)

    # Skip the header row
    header = next(reader)
    
    for row in reader:
    # Collect data for analysis
        months.append(row[0])
        profit_losses.append(int(row[1]))

#calculate the total number of months 
        total_months = len(months)

#calculate the net total of "Profit/Losses"
        net_total = sum(profit_losses)

# Calculate monthly changes
        monthly_changes = []
        for i in range(1, len(profit_losses)):
            change = profit_losses[i] - profit_losses[i - 1]
            monthly_changes.append(change)

# Average of changes
average_change = sum(monthly_changes) / len(monthly_changes)

 # Calculate the greatest increase in profits (month and amount)
greatest_increase = max(monthly_changes)
greatest_increase_date = months[monthly_changes.index(greatest_increase) + 1]

# Calculate the greatest decrease in losses (month and amount)
greatest_decrease = min(monthly_changes)
greatest_decrease_date = months[monthly_changes.index(greatest_decrease) + 1]

# Print the output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
