scores = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6,
}

with open("input2-1.txt") as f:
    score = 0
    for line in f:
        line = line.strip()
        score += scores[line]
        print(score)