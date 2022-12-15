import re

with open("input4-1.txt") as f:
    score = 0
    for line in f:
        line = line.strip()
        m = re.match('(\d+)-(\d+),(\d+)-(\d+)',line)
        if not m:
            print('Parse error')
            exit(-1)
        leftA = int(m.group(1))
        leftB = int(m.group(2))
        rightA = int(m.group(3))
        rightB = int(m.group(4))
        if leftA <= rightA and rightB <= leftB:
            # left contains right
            score +=1
        elif rightA <= leftA and leftB <= rightB:
            # right contains left
            score +=1
        elif rightA <= leftB and rightB >= leftB:
            # right begins before left ends
            score +=1
        elif leftA <= rightB and leftB >= rightB:
            # left begins before right ends
            score +=1
        print(score)