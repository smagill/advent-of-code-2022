import re
import numpy as np
from dijkstar import Graph, find_path
import functools

def convert(left,right):
    if isinstance(left,int) and isinstance(right,list):
        left = [left]
    if isinstance(right,int) and isinstance(left,list):
        right = [right]
    if isinstance(left,int):
        return (left,right)
    newleft = list()
    newright = list()
    extent = min(len(left),len(right))
    for i in range(0,extent):
        (left_item,right_item) = convert(left[i],right[i])
        newleft.append(left_item)
        newright.append(right_item)
    newleft += left[extent:]
    newright += right[extent:]
    return (newleft,newright)

def compare(left,right):
    (left,right) = convert(left,right)
    if left < right:
        return 1
    if right < left:
        return -1
    return 0

with open("input13-1.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    lines = list(filter(lambda x: x, lines))
    lines = list(map(eval,lines))
    lines.append([[2]])
    lines.append([[6]])

    lines.sort(key=functools.cmp_to_key(compare),reverse=True)
    for line in lines:
        print(line)

    index1 = lines.index([[2]])+1
    index2 = lines.index([[6]])+1
    print(index1 * index2)