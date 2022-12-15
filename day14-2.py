import re
import numpy as np
from dijkstar import Graph, find_path
import functools

grid = dict()

min_x = 0
min_y = 0
max_x = 0
max_y = 0
floor_y = 0

def draw_line(c1,c2):
    [x1,y1] = c1
    [x2,y2] = c2
    if x1 == x2:
        ystart = min(y1,y2)
        yend = max(y1,y2)
        for y in range(ystart,yend+1):
            grid[(x1,y)] = '#'
    elif y1 == y2:
        xstart = min(x1,x2)
        xend = max(x1,x2)
        for x in range(xstart,xend+1):
            grid[(x,y1)] = '#'
    else:
        print('ERROR: Line is not horizontal or vertical.')

def drop_sand(sand_x,sand_y):
    if sand_y + 1 == floor_y:
        print('Sand hit the floor')
        grid[(sand_x,sand_y)] = 'o'
        return (sand_x,sand_y)
    if (sand_x,sand_y+1) not in grid:
        return drop_sand(sand_x,sand_y+1)
    elif (sand_x-1,sand_y+1) not in grid:
        return drop_sand(sand_x-1,sand_y+1)
    elif (sand_x+1,sand_y+1) not in grid:
        return drop_sand(sand_x+1,sand_y+1)
    else:
        grid[(sand_x,sand_y)] = 'o'
        return (sand_x,sand_y)

def trace_sand(sand_x,sand_y):
    grid[(sand_x,sand_y)] = '~'
    if sand_y > max_y:
        print('Sand fell out')
        return True
    if (sand_x,sand_y+1) not in grid:
        return trace_sand(sand_x,sand_y+1)
    elif (sand_x-1,sand_y+1) not in grid:
        return trace_sand(sand_x-1,sand_y+1)
    elif (sand_x+1,sand_y+1) not in grid:
        return trace_sand(sand_x+1,sand_y+1)
    else:
        grid[(sand_x,sand_y)] = 'o'
        return False

def update_maxs():
    global min_x, min_y, max_x, max_y
    coords = grid.keys()
    min_x = min(map(lambda c: c[0], coords))
    min_y = min(map(lambda c: c[1], coords))
    max_x = max(map(lambda c: c[0], coords))
    max_y = max(map(lambda c: c[1], coords))

def draw_grid():
    update_maxs()
    for y in range(min_y,max_y+1):
        for x in range(min_x,max_x+1):
            if (x,y) not in grid:
                print('.',end='')
            else:
                print(grid[(x,y)],end='')
        print()
    print()

with open("input14-1.txt") as f:
    for line in f.readlines():
        line = line.strip()
        coords = line.split(' -> ')
        coords = list(map(lambda x: list(map(int,x.split(','))), coords))

        for i in range(0,len(coords)-1):
            draw_line(coords[i], coords[i+1])

    update_maxs()
    floor_y = max_y + 2
    draw_grid()

    count = 0
    while True:
        sand_coord = drop_sand(500,0)
        count += 1
        print(count)
        #draw_grid()
        if sand_coord == (500,0):
            break
    
    draw_grid()
    
    print('Total sand:',count)