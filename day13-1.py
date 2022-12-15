import re
import numpy as np
from dijkstar import Graph, find_path

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

with open("input13-1.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    lines.reverse()

    index = 0
    sum = 0
    while lines:
        index += 1
        left = lines.pop()
        right = lines.pop()
        if lines:
            lines.pop()
        left_val = eval(left)
        right_val = eval(right)
        print(left_val)
        print(right_val)
        (left_val,right_val) = convert(left_val,right_val)
        print(left_val)
        print(right_val)
        if left_val <= right_val:
            sum += index
        print(sum)