import os 
import csv

csvpath = os.path.join('.', 'Resources', 'poll.csv')
# read csv file as a list of lists
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    # remove header line
    csv_header=next(csv_reader)
    list_of_rows=list(csv_reader)
print("Election Results")
print("-------------------------------")
# find total number of month by counting the rows without header

total_votes= len(list_of_rows)
print("Total votes:" , total_votes)
print("------------------------------")
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

print("Khan:", formatted_percent_khan, formatted_count_khan)
print("Correy:", formatted_percent_Correy,formatted_count_Corry)
print("Li:", formatted_percent_Li,formatted_count_Li)
print("O'Tooley:",formatted_percent_O,formatted_count_O)

print('------------------------------------------------')

# print the winner by looking at who has the largest number of votes
if (count_Khan>count_Correy and count_Khan>count_Li and count_Khan>count_O):
    print("Winner: Khan")
elif count_Correy > count_Khan and count_Correy > count_Li and count_Correy > count_O:
    print("Winner:Correy")
elif count_Li>count_Khan and count_Li>count_Correy and count_Li>count_O:
    print("Winner:Li")
elif count_O > count_Khan and count_O > count_Correy and count_O >count_Li:
    print("Winner: O'Tooley")
print('-------------------------------------------------')


# bonus py paragraph 
#open paragraph txt
textfile= os.path.join('.', 'Resources', 'paragraph.txt')
with open('textfile')as f:
    content=f.read()
# count number of word
word_count = len(content.split()) 
print("Paragraph Analysis")
print("---------------------------")
print('Approximate word conut:',str(word_count))

# count the number of sentence by counting . in the paragrap
with open('textfile')as f:
    data=f.read()
    print('Total Sentences:', data.count('.'))


# split paragraph into words
words=content.split()
# calculate total length of words
lengths=[len(word)for word in words]
#calculate average length
average_length=sum(lengths)/len(lengths)
#format average length
formatted_length_average="{:.1f}".format(average_length)

print('Average letter count:', formatted_length_average )

countword=[]
with open('textfile')as f:
    txt=f.read()
    Sentences=txt.split('.')
    for sent in Sentences:
        wordss=sent.split()
        countword.append(len(wordss))
average_countword=sum(countword)/len(countword)
#format to one decimal place
formatted_average="{:.1f}".format(average_countword)
print('Average Sentence Length:',formatted_average)