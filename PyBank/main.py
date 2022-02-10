# Import Dependencies
import os
import csv
from telnetlib import OUTMRK

# Relative Path to file
csv_path = os.path.join("Resources/budget_data.csv")
text_path = os.path.join("Analysis/financial_analysis.txt")

# Initializing variables
total_months = 0
net_total = 0
month_change = []
net_change_list = []
greatest_increase=["", 0]
greatest_decrease=["", 99999999999999]



with open (csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Bypass the header
    csv_header = next(csvreader)
    first_row = next(csvreader)

    #set first row for Jan
    print(first_row)

    total_months += 1
    print(total_months)

    net_total += int(first_row[1])
    print(net_total)

    previous_net = int(first_row[1])
    print(previous_net)

    # Start itirating with Feb
    for row in csvreader:
        
        # Update total_months
        total_months += 1
        net_total += int(row[1])

       # Calculate net change
        net_change = int(row[1]) - previous_net

       #Set prev net for next month
        previous_net = int(row[1])

       # Add month to month_change list
        month_change += [row[0]]

       # add net change to net_change_list
        net_change_list += [net_change]

       # Calculate the greatest increase
    if net_change > greatest_increase[1]:
           greatest_increase[0] = row[0]
           greatest_increase[1] = net_change
       
       # Calculate the greatest decrease
    if net_change < greatest_decrease[1]:
           greatest_decrease[0] = row[0]
           greatest_decrease[1] = net_change


# Calculate Average Change
average_monthly_change = sum(net_change_list)/ len(net_change_list)


# Generate Summary
Output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {net_total}\n" 
    f"Average  Change: ${average_monthly_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    
)
# Print to Terminal
print(Output)


# export a text file
with open (text_path, "w") as txt_file:
    txt_file.write(Output)
