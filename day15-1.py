import re
import numpy as np
from dijkstar import Graph, find_path
import functools

class Grid(dict):
    def __init__(self,*arg,**kw):
        super(Grid, self).__init__(*arg, **kw)
        self.min_x = 0
        self.min_y = 0
        self.max_x = 0
        self.max_y = 0
    
    def __setitem__(self, key, item):
        super(Grid,self).__setitem__(key,item)
        if key[0] < self.min_x:
            self.min_x = key[0]
        if key[0] > self.max_x:
            self.max_x = key[0]
        if key[1] < self.min_y:
            self.min_y = key[1]
        if key[1] > self.max_y:
            self.max_y = key[1]

    def __getitem__(self, key):
        if key not in super(Grid,self).keys():
            return '.'
        else:
            return super(Grid,self).__getitem__(key)

    def __str__(self):
        str = list()
        for y in range(self.min_y,self.max_y+1):
            for x in range(self.min_x,self.max_x+1):
                if (x,y) not in grid:
                    str.append('.')
                else:
                    str.append(grid[(x,y)])
            str.append('\n')
        return ''.join(str)
    
    def get_row(self,row):
        ret = list()
        for i in range(self.min_x,self.max_x+1):
            ret.append(self[i,row])
        return ''.join(ret)

grid = Grid()

def color_range(x,y,d):
    for y_offset in range(-d,d+1):
        print('y_offset',y_offset)
        remaining = d - abs(y_offset)
        for x_offset in range(-remaining,remaining+1):
            if grid[(x+x_offset,y+y_offset)] == '.':
                grid[(x+x_offset,y+y_offset)] = '#'

with open("input15-1.txt") as f:
    for line in f.readlines():
        line = line.strip()
        print(line)
        m = re.match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)',line)
        if not m:
            print("Parse error:\n   ",line)
        sx = int(m.group(1))
        sy = int(m.group(2))
        bx = int(m.group(3))
        by = int(m.group(4))

        print(sx,sy,bx,by)
        grid[sx,sy] = 'S'
        grid[bx,by] = 'B'

        #print(grid)
        dist = abs(bx - sx) + abs(by - sy)
        color_range(sx,sy,dist)
        #print(grid)
    
    #print(grid)

    #print(grid.get_row(10))
    print('count =',len(list(filter(lambda x: x == '#',grid.get_row(10)))))