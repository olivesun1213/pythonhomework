
import os
print("Paragraph Analysis")
print("---------------------------")
#import and read file
textfile=os.path.join('.', 'Resources', 'paragraph.txt')
f=open(textfile,'r')

# count number of words and number of sentences by counting space and .
with open(textfile) as f:
    content=f.read()
    wordcount=len(content.split())
    print('Approximate word conut:',str(wordcount))
    print('Total Sentences:', content.count('.'))

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
with open(textfile)as f:
    txt=f.read()
    Sentences=txt.split('.')
    for sent in Sentences:
        wordss=sent.split()
        countword.append(len(wordss))
average_countword=sum(countword)/len(countword)
#format to one decimal place
formatted_average="{:.1f}".format(average_countword)
print('Average Sentence Length:',formatted_average)