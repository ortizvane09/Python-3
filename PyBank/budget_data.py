import csv
import os
budget_csv = os.path.join('Resources', 'budget_data.csv')
Total_Months = 0
Month_Of_Change = []
Changes_Profit_Losses = []
Max_Increase = ["", 0]
Max_Decrease = ["", 9999999999999999999]
Total_Net = 0

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    first_row = next(csvreader)
    Total_Months += 1
    Total_Net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:
        Total_Months += 1
        Total_Net += int(row[1])
        Net_Change = int(row[1]) - prev_net
        prev_net = int(row[1])
        Changes_Profit_Losses += [Net_Change]
        Month_Of_Change += [row[0]]

        if Net_Change > Max_Increase[1]:
            Max_Increase[0] = row[0]
            Max_Increase[1] = Net_Change

        if Net_Change < Max_Decrease[1]:
            Max_Decrease[0] = row[0]
            Max_Decrease[1] = Net_Change  

    Average_Change = sum(Changes_Profit_Losses)/ len(Changes_Profit_Losses)

output = (f"Total_Months: {Total_Months}\n"
          f"Total_Net: ${Total_Net}\n"
          f"Average_Change: ${Average_Change:.2f}\n"
         f"Max_Increase in Profits: {Max_Increase[0]} (${Max_Increase[1]})\n" 
         f"Max_Decrease in Profits: {Max_Decrease[0]} (${Max_Decrease[1]})\n" )

print("Financial Analysis")
print("__________________________________")
print(output)