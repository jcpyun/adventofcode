# 2020_2.py
import csv
def counter(sentence,char):
    counter = 0
    for s in sentence:
        if s == char:
            counter+=1
    return counter

# pt 1
# with open('2020_2.csv') as csvfile:
#     reader = csv.reader(csvfile , delimiter=' ')
#     count = 0
#     for row in reader:
#         sentence=row[2]
#         char=row[1][0]
#         min=int(row[0].split('-')[0])
#         max=int(row[0].split('-')[1])
#         if counter(sentence, char) >= min and counter(sentence, char) <= max:
#             count+=1
#     print(count)

#pt2
with open('2020_2.csv') as csvfile:
    reader = csv.reader(csvfile , delimiter=' ')
    count = 0
    for row in reader:
        sentence=row[2]
        char=row[1][0]
        left=int(row[0].split('-')[0])
        right=int(row[0].split('-')[1])
        
 
        if sentence[left-1] == char and sentence[right-1] != char:
            count += 1
      
        elif sentence[left-1] != char and sentence[right-1] == char:
            count += 1
    print(count)