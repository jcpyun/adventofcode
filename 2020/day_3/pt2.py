# pt 2
import csv

column=0
row=0
multi_count=1

pattern = [[1,1], [3,1], [5,1], [7,1], [1,2]]

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

grid = []
with open('2020_3.csv') as csvfile:
    reader = csv.reader(csvfile)
    tree_count = 0
    right_counter = 0
    for r in reader:
        grid.append(list(r[0]))

for p in pattern:
    count=0
    print(p[0], p[1])
    column=0
    row=0
    while row < len(grid)-1:
        column+=p[0]
        row+=p[1]
        
        if grid[row][column % len(grid[0])] == '#':
            count += 1

    multi_count *= count
print(multi_count)