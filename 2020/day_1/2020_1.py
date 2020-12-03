# 2020_1.py
import csv
with open('2020_1.csv') as csvfile:
    reader = csv.reader(csvfile)
    varr = []
    # for row in reader:
    #     v = int(row[0])
    #     if 2020 - v not in varr:
    #         varr.append(v)
    #     else:
    #         print(v, 2020-v, v*(2020-v))
    # print(reader)
    data = []
    for row in reader:
        data.append(int(row[0]))
    for x in range(len(data)):
        target = 2020-data[x]
        cur=[]
        for y in range(x+1,len(data)):
            # print(data[x])
            if target - data[y] not in cur:
                cur.append(data[y])
            else:
                print(data[x]*data[y]* (2020-data[x]-data[y]))
    # for x in range(5):
    #     for y in range(x+1,5):
    #         print(x,y)
        
