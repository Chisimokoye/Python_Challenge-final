from itertools import count
import os 
import csv 

csv_path = os.path.join("..","..", "Python-Challenge", "Pybank", "resources", "budget_data.csv")
month = []
profit_loss = []
monthly_changes = []
row = []

count_mth = 0
net_P_L = 0
P_L_change =0
begining_profit = 0 


with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    #print (csvreader)
    #read header row first
    csv_header = next(csvreader)
    print(f'CSV header: {csv_header}')

    
    

    for row in csvreader:
        count_mth += 1
        month.append(row[0])
        profit_loss.append(row[1])
        net_P_L = net_P_L + int(row[1])
        final_profit =int(row[1])
        month_change = final_profit - begining_profit
        monthly_changes.append(month_change) 
        P_L_change = P_L_change + month_change
        begining_profit = final_profit



average_P_L = round((month_change/count_mth), 2)
highest_profit = max(monthly_changes)
lowest_profit = min(monthly_changes)
highest_month = month[monthly_changes.index(highest_profit)]
lowest_month = month[monthly_changes.index(lowest_profit)]
    

print('Financial Analysis')
print('-------------------------------------------------------------')
print(f'Total Months: {count_mth}')
print(f'Net Total: ${net_P_L}')
print(f'Average Change: ${average_P_L}')
print(f'Greatest Increase in Profits:{highest_month} ${highest_profit}')
print(f'Greatest Decrease in Profits: {lowest_month}  ${lowest_profit}')


Output_path = os.path.join("..","..", "Python-Challenge", "Pybank", "resources", "budget_data.txt")
with open(Output_path, 'w') as textfile:



    textfile.write('Financial Analysis')
    textfile.write('-------------------------------------------------------------')
    textfile.write(f' Total Months: {count_mth}')
    textfile.write(f' Net Total: ${net_P_L}')
    textfile.write(f'Average Change: ${average_P_L}')
    textfile.write(f'Greatest Increase in Profits:{highest_month} ${highest_profit}')
    textfile.write(f'Greatest Decrease in Profits: {lowest_month}  ${lowest_profit}')


