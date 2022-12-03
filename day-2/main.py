scores = {
    "X": {
        "A": 3,
        "B": 0,
        "C": 6
    },
    "Y": {
        "A": 6,
        "B": 3,
        "C": 0
    },
    "Z": {
        "A": 0,
        "B": 6,
        "C": 3
    }
}

scoreMapping = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

outcomeMapping = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

def complementSign(sign, state):
    if sign == "A": # opponent rock
        # return rock if we need to draw
        return "X" if state == "Y" else "Y" if state == "Z" else "Z"
    elif sign == "B": # opponent paper
        # return paper if we need to draw, scissor for win
        return "Y" if state == "Y" else "Z" if state == "Z" else "X"
    else: # opponent scissor
        # return scissor if we need to draw, rock for win
        return "Z" if state == "Y" else "X" if state == "Z" else "Y"

def computeScore(opponent, me):
    score = 1 if me == "X" else 2 if me == "Y" else 3
    score += scores[me][opponent]

    return score


with open("input.txt", "r") as file:
    total = 0
    lines = file.read().split("\n")

    for i in range(len(lines)):
        line = lines[i].split(" ")
        opponent, luck = line

        me = complementSign(opponent, luck)
        total += scoreMapping[me] + outcomeMapping[luck]
        # total += computeScore(line[0], line[1])

    print(total)