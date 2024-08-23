# This will allow us to create file path across operating systems
import os

# Module for reading CSV files
import csv

# Initialize variables for all of the calulated totals
total_months = 0
net_total_amount = 0
total_amount = 0
greatest_increase_date = 0
greatest_increase_amount = 0
greatest_decrease_date = 0
greatest_decrease_amount = 0
previous_profit = 0
profit_losses = []

# The 'Resources' directory containing the 'budget_data.csv' records that is being analyzed
csvpath = os.path.join('Resources', 'budget_data.csv')

# The 'analysis' directory containing the output of the analysis to a 'results.txt' text file
txtpath = os.path.join('analysis', 'results.txt')

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies the comma delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csv_reader)
    
    # Setting the date column as column 1 and the price column as column 2 
    date_index = 0
    price_index = 1

    # Read each row of data after the header
    for row in csv_reader:
        
        # Keep track of the total number of months
        total_months += 1

        # Keep track of the total amount and finds the sum
        net_total_amount = int(row[price_index])
        total_amount += net_total_amount

        # Sets current date to value from the first column and the 
        # current profit to the valua from the second column
        current_date = row[date_index]
        current_profit = int(row[price_index])

        # Checks if the previous ptofit is not zero
        if previous_profit != 0:
            # Calculate the profit change by computing the difference 
            # between the current profit and the previous profit
            profit_change = current_profit - previous_profit
            # Track the profit change from the profit losses list
            profit_losses.append(profit_change)

            # If the current profit change is greater than the previous one, update greatest 
            # increase to the new profit change and records the date of the increase
            if profit_change > greatest_increase_amount:
                greatest_increase_amount = profit_change
                greatest_increase_date = current_date

            # If the profit change is less than the previous one, update greatest decrease to 
            # the new profit change and records the date of the decrease
            if profit_change < greatest_decrease_amount:
                greatest_decrease_amount = profit_change
                greatest_decrease_date = current_date
            
        # Update the previous profit to the current profit for the next interation    
        previous_profit = current_profit

# Average change in profits
average_change = sum(profit_losses)/len(profit_losses)

# Print the analysis to the terminal window
print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})')

# Output the analysis to a text file named 'results.txt" in the 'analysis' director
with open(txtpath, 'w') as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_amount}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")
