

#open paragraph txt

import os
textfile=os.path.join('.', 'Resources', 'paragraph.txt')
with open(textfile) as f:
    content=f.read

# count number of word
word_count = len(content.split()) 
print("Paragraph Analysis")
print("---------------------------")
print('Approximate word conut:',str(word_count))

# count the number of sentence by counting . in the paragrap
with open(textfile)as f:
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