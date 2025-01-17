f=open('poll_analysis.txt',"a")
import os 
import csv

csvpath = os.path.join('.', 'Resources', 'poll.csv')
# read csv file as a list of lists
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    # remove header line
    csv_header=next(csv_reader)
    list_of_rows=list(csv_reader)
print("Election Results",file=f)
print("-------------------------------",file=f)
# find total number of month by counting the rows without header

total_votes= len(list_of_rows)
print("Total votes:" , total_votes,file=f)
print("------------------------------",file=f)
#create a new column called vote that transfer column C into String
vote=[]
for row in list_of_rows[2:]:
    vote.append(str(row[2]))

#count the number of vote based on name
count_Khan = vote.count('Khan')
count_Correy = vote.count('Correy')
count_Li=vote.count('Li')
count_O= total_votes-count_Correy-count_Khan-count_Li

# find the percent of vote by using name vote/total vote
percent_Khan=(count_Khan/total_votes)
percent_Correy=(count_Correy/total_votes)
percent_Li=(count_Li/total_votes)
percent_O=(count_O/total_votes)

#format the percent vote to three decimal and add %
formatted_percent_khan="{:.3%}".format(percent_Khan)
formatted_percent_Correy ="{:.3%}".format(percent_Correy)
formatted_percent_Li="{:.3%}".format(percent_Li)
formatted_percent_O="{:.3%}".format(percent_O)
#format vote count by adding ()
formatted_count_khan="({})".format(count_Khan)
formatted_count_Corry="({})".format(count_Correy)
formatted_count_Li="({})".format(count_Li)
formatted_count_O="({})".format(count_O)

print("Khan:", formatted_percent_khan, formatted_count_khan,file=f)
print("Correy:", formatted_percent_Correy,formatted_count_Corry,file=f)
print("Li:", formatted_percent_Li,formatted_count_Li,file=f)
print("O'Tooley:",formatted_percent_O,formatted_count_O,file=f)

print('------------------------------------------------',file=f)

# print the winner by looking at who has the largest number of votes
if (count_Khan>count_Correy and count_Khan>count_Li and count_Khan>count_O):
    print("Winner: Khan",file=f)
elif count_Correy > count_Khan and count_Correy > count_Li and count_Correy > count_O:
    print("Winner:Correy",file=f)
elif count_Li>count_Khan and count_Li>count_Correy and count_Li>count_O:
    print("Winner:Li",file=f)
elif count_O > count_Khan and count_O > count_Correy and count_O >count_Li:
    print("Winner: O'Tooley",file=f)
print('-------------------------------------------------',file=f)
f.close()


