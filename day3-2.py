def priority(letter):
    if ord(letter) <= ord('Z'):
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1

with open("input3-1.txt") as f:
    score = 0
    lines = f.readlines()
    for i in range(0,len(lines),3):
        common = set(lines[i].strip()).intersection(set(lines[i+1].strip())).intersection(set(lines[i+2].strip()))
        print(common)
        score += priority(common.pop())
        print(score)