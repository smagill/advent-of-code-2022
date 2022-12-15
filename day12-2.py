import re
import numpy as np
from dijkstar import Graph, find_path

grid = list()
graph = Graph()

def valid_step(row,col,newrow,newcol):
    if newrow < 0 or newcol < 0:
        return False
    if newrow >= len(grid) or newcol >= len(grid[newrow]):
        return False
    if ord(grid[newrow][newcol]) <= ord(grid[row][col]) + 1:
        return True
    else:
        return False

start_pos = set()

with open("input12-1.txt") as f:
    for line in f.readlines():
        grid.append(line.strip())

    for row in range(0,len(grid)):
        for col in range(0,len(grid[row])):
            if grid[row][col] == 'S':
                grid[row] = grid[row][0:col] + 'a' + grid[row][col+1:]
            if grid[row][col] == 'E':
                end_pos = (row,col)
                grid[row] = grid[row][0:col] + 'z' + grid[row][col+1:]
    
    for row in grid:
        print(row)

    for row in range(0,len(grid)):
        for col in range(0,len(grid[row])):
            if grid[row][col] == 'a':
                start_pos.add((row,col))

    for row in range(0,len(grid)):
        for col in range(0,len(grid[row])):
            for row_offset in [-1,1]:
                if valid_step(row,col,row+row_offset,col):
                    print('Adding edge',(row,col),'to',(row+row_offset,col))
                    graph.add_edge((row,col),(row+row_offset,col),1)
            for col_offset in [-1,1]:
                if valid_step(row,col,row,col+col_offset):
                    print('Adding edge',(row,col),'to',(row,col+col_offset))
                    graph.add_edge((row,col),(row,col+col_offset),1)
    
    costs = list()
    for start in start_pos:
        try:
            path = find_path(graph,start,end_pos)
            costs.append(path.total_cost)
        except:
            continue

    print(costs)
    print(min(costs))