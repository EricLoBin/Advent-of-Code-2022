from inputs.input import get_input

inp = get_input(2).read().split("\n")

score = 0

for i in inp:
    match i[2]:
        case "X": # lose
            score += 0
            if i[0] == "A": # opponent plays rock
                score += 3
            elif i[0] == "B": # opponent plays paper
                score += 1
            elif i[0] == "C": # opponent plays scissors
                score += 2

        case "Y": # draw
            score += 3
            if i[0] == "A": # opponent plays rock
                score += 1
            elif i[0] == "B": # opponent plays paper
                score += 2
            elif i[0] == "C": # opponent plays scissors
                score += 3

        case "Z": # win
            score += 6
            if i[0] == "A": # opponent plays rock
                score += 2
            elif i[0] == "B": # opponent plays paper
                score += 3
            elif i[0] == "C": # opponent plays scissors
                score += 1

print(score)
