import csv

column=0
row=0
count=0

grid = []
with open('2020_3.csv') as csvfile:
    reader = csv.reader(csvfile)
    tree_count = 0
    right_counter = 0
    for r in reader:
        grid.append(list(r[0]))

while row < len(grid)-1:
    column+=3
    row+=1
    if grid[row][column % len(grid[0])] == '#':
            count += 1
print(count)

