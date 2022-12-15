import re

def scenic(grid,row,col,row_offset,col_offset):
    height = grid[row][col]
    row += row_offset
    col += col_offset
    score = 0
    while row >= 0 and row < len(grid) and col >= 0 and col < len(grid[row]):
        score += 1
        if grid[row][col] >= height:
            break
        row += row_offset
        col += col_offset
    return score

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
    scores = list()
    for row in range(0,len(grid)):
        for col in range(0,len(grid[row])):
            score = scenic(grid,row,col,0,-1) * scenic(grid,row,col,-1,0) \
               * scenic(grid,row,col,0,1) * scenic(grid,row,col,1,0)
            scores.append(score)
    
    print(max(scores))