import re
import numpy as np

important_times = set(range(20,221,40))

with open("input10-1.txt") as f:
    x = 1
    cycle = 1
    sum = 0
    for line in f.readlines():
        print(cycle,x,sep='\t')
        line = line.strip()
        print(line)
        m = re.match('addx (-?\d+)',line)
        if m:
            newx = x + int(m.group(1))
            newcycle = cycle + 2
        m = re.match('noop',line)
        if m:
            newx = x
            newcycle = cycle + 1
        prevx_times = set(range(cycle,newcycle))
        if important_times.intersection(prevx_times):
            key_cycle = important_times.intersection(prevx_times).pop()
            strength = x * key_cycle
            print(key_cycle,strength)
            sum += x * important_times.intersection(prevx_times).pop()
        cycle = newcycle
        x = newx
    print(sum)