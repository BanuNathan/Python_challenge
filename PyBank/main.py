import os
import csv

months=[]
profit_loss=[]
Monthly_profit_loss_change=[]

#open input file
budget_data_csv = os.path.join( "Resources", "budget_data.csv")

#open output file 
output_file = os.path.join("Analysis","Fin_analysis.txt")

with open(budget_data_csv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header and store values in CVS_header
    csv_header = next(csvfile)

    # append the months from the input file into a list months[]
    for row in csvreader:
        # Add month to months
        months.append(row[0])
        #add to profit loss list
        profit_loss.append(int(row[1]))
    
    # calculate the change in profit/loss between successive months and store in the list
    for i in range(len(profit_loss)-1):
        Monthly_profit_loss_change.append((profit_loss[i+1]-profit_loss[i]))

    # Calculate the maximum change in monthly profit/loss change
    for i in range(len(months)):
        if Monthly_profit_loss_change[i] == max(Monthly_profit_loss_change):
            max_month_index=i+1
            break

    # Calculate the minimum change in monthly profit/loss change
    for i in range(len(months)):
        if Monthly_profit_loss_change[i] == min(Monthly_profit_loss_change):
            min_month_index=i+1
            break
    
# write to output text file
output_file1 = open(output_file,"w")
output_file1.write('Financial Analysis of PyBank\n')
output_file1.write('----------------------------\n')
output_file1.write('Total Months  ')            
output_file1.write(str(len(months)))
output_file1.write('\n')
output_file1.write('Total ')
output_file1.write(str(sum(profit_loss)))
output_file1.write('\n')
output_file1.write('Average ')
output_file1.write(str(round(sum(Monthly_profit_loss_change) / len(Monthly_profit_loss_change), 2)))
output_file1.write('\n')
output_file1.write('Greatest increase in profit  ')
output_file1.write(months[max_month_index])
output_file1.write('   ')
output_file1.write(str(max(Monthly_profit_loss_change)))
output_file1.write('\n')
output_file1.write('Greatest decrease in profit  ')
output_file1.write(months[min_month_index])
output_file1.write('   ')
output_file1.write(str(min(Monthly_profit_loss_change)))




#print to the terminal
print("Financial Analysis")
print("--------------------------")
print(f"Total Months : {len(months)}")
print(f"Total :${sum(profit_loss)}")
print(f"Average  : { round(sum(Monthly_profit_loss_change) / len(Monthly_profit_loss_change), 2)}")
print(f"Greatest increase in profits: {months[max_month_index]}   (${max(Monthly_profit_loss_change)})")
print(f"Greatest decrease in profits: {months[min_month_index]}   (${min(Monthly_profit_loss_change)})")
print("--------------------------")

