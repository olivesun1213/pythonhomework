
f=open('bank_analysis.txt',"a")
import os 
import csv

csvpath = os.path.join('.', 'Resources', 'bank.csv')
# read csv file as a list of lists
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    print(csv_reader)
    #remove header
    csv_header=next(csv_reader)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
# find total number of month by counting the rows without header
total_month= len(list_of_rows)
print("Financial Analysis",file=f)
print("---------------------------------",file=f)
print("Total Months:" + str(total_month),file=f)

#calculate total volume
volume= []
#convert profit/loss into integer
for row in list_of_rows[1:]:
    volume.append(int(row[1]))
#sum all volume
vol_sum = sum(volume)
print('Total: $', vol_sum,file=f)

# make a column called temp(changes in profit) by looking at difference between the rows
import numpy as np 
temp=np.array(volume)
tempdiff=np.diff(temp,axis=0)
# find the average of changes (total difference)/(month-1)
avgchanges=float((sum(tempdiff))/(total_month-1))
#round the average change to 2 decimal places
round_avg_changes=round(avgchanges,2)
print("Average Change: $ ", round_avg_changes,file=f)

# find the index of max value and subtract 1 to find actual max index
max_value=np.argmax(temp,axis=0)
max_value_index=max_value-1

#only show first value in list of rows data (only get the date not the profit/loss)
first_value=list(zip(*list_of_rows))[0]
# find the date and change of the greates increase in profit
max_value_date=first_value[max_value+1]
max_value_change=tempdiff[max_value_index]
print("Greatest increase in profit:", max_value_date, '(${})'.format(max_value_change),file=f)

# find the index of min value and subtract 1 to find actual min index
min_value=np.argmin(temp,axis=0)
min_value_index=min_value-1
#only show first value in list of rows data (only get the date not the profit/loss)
first_value=list(zip(*list_of_rows))[0]
# find the date and change of the greates increase in profit
min_value_date=first_value[min_value+1]
min_value_change=tempdiff[min_value_index]
print("Greatest decrease in profit:", min_value_date, ('(${})'.format(min_value_change)),file=f)
f.close()