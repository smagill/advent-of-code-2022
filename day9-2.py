import re
import numpy as np

left = np.array([-1,0])
right = np.array([1,0])
up = np.array([0,1])
down = np.array([0,-1])
origin = np.array([0,0])

def tail_pos(rope):
    return rope[-1].tobytes()

with open("input9-1.txt") as f:
    visited = dict()
    rope = [np.copy(origin) for i in range(0,10)]
    visited[tail_pos(rope)] = 1
    moves = 0

    for line in f.readlines():
        line = line.strip()
        dir = line[0]
        num = int(line[2:])
        for i in range(0,num):
            moves += 1
            print(rope[0],rope[-1])
            print(dir)
            if dir == 'R':
                rope[0] += right
            elif dir == 'L':
                rope[0] += left
            elif dir == 'U':
                rope[0] += up
            elif dir == 'D':
                rope[0] += down
            for segment in range(1,len(rope)):
                diff = rope[segment-1] - rope[segment]
                if abs(diff[0]) <= 1 and abs(diff[1]) <= 1:
                    # close enough -- nothing to do
                    print('no move required')
                else:
                    # move 1 step in direction of head
                    rope[segment] += diff // abs(diff)
                    print('moving segment',segment,'to:',rope[segment])
                if abs(rope[segment-1] - rope[segment])[0] > 1 or abs(rope[segment-1] - rope[segment])[1] > 1:
                    print("hmm, something is wrong")
            visited[tail_pos(rope)] = 1
    print('visited:',len(visited))
    print('moves:',moves)