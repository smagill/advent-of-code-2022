import re

def visible(grid,row,col,row_offset,col_offset):
    height = grid[row][col]
    row += row_offset
    col += col_offset
    while row >= 0 and row < len(grid) and col >= 0 and col < len(grid[row]):
        if grid[row][col] >= height:
            return False
        row += row_offset
        col += col_offset
    return True

with open("input8-1.txt") as f:
    grid = list()
    for line in f.readlines():
        line = line.strip()
        row = list()
        for c in line:
            row.append(int(c))
        grid.append(row)
    print(grid)

    sum = 0
    for row in range(0,len(grid)):
        for col in range(0,len(grid[row])):
            if visible(grid,row,col,0,-1) or visible(grid,row,col,-1,0) \
               or visible(grid,row,col,0,1) or visible(grid,row,col,1,0):
               sum += 1
    
    print(sum)