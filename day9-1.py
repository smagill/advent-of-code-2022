import re
import numpy as np

left = np.array([-1,0])
right = np.array([1,0])
up = np.array([0,1])
down = np.array([0,-1])
origin = np.array([0,0])

with open("input9-1.txt") as f:
    visited = dict()
    head = np.copy(origin)
    tail = np.copy(origin)
    visited[tail.tobytes()] = 1
    moves = 0

    for line in f.readlines():
        line = line.strip()
        dir = line[0]
        num = int(line[2:])
        for i in range(0,num):
            moves += 1
            print(head,tail)
            print(dir)
            if dir == 'R':
                head += right
            elif dir == 'L':
                head += left
            elif dir == 'U':
                head += up
            elif dir == 'D':
                head += down
            diff = head - tail
            if abs(diff[0]) <= 1 and abs(diff[1]) <= 1:
                # close enough -- nothing to do
                print('no move required')
            else:
                # move 1 step in direction of head
                tail += diff // abs(diff)         
                print('moving tail to:',tail)
            if abs(head - tail)[0] > 1 or abs(head - tail)[1] > 1:
                print("hmm, something is wrong")
            visited[tail.tobytes()] = 1
    print('visited:',len(visited))
    print('moves:',moves)