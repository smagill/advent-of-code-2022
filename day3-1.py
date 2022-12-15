def priority(letter):
    if ord(letter) <= ord('Z'):
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1

with open("input3-1.txt") as f:
    score = 0
    for line in f:
        line = line.strip()
        size = len(line)
        midpoint = int(size/2)
        left = line[:midpoint]
        right = line[midpoint:]
        common = set(left).intersection(set(right))
        score += priority(common.pop())
        print(score)