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

win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

loss = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

with open("input2-1.txt") as f:
    score = 0
    for line in f:
        line = line.strip()
        opp_play = line[0]
        result = line[2]
        if result == 'X':
            # lose
            play = loss[opp_play]
        elif result == 'Y':
            # draw
            play = draw[opp_play]
        else:
            # win
            play = win[opp_play]
        score += scores[line[0] + ' ' + play]
        print(score)