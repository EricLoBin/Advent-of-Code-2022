from inputs.input import get_input

inp = get_input(2).read().split("\n")

score = 0

for i in inp:
    match i[2]:
        case "X": # rock
            score += 1
            if i[0] == "A": # rock
                score += 3
            elif i[0] == "C": # scissors
                score += 6

        case "Y": # paper
            score += 2
            if i[0] == "A": # rock
                score += 6
            elif i[0] == "B": # paper
                score += 3

        case "Z": # scissors
            score += 3
            if i[0] == "B": # paper
                score += 6
            elif i[0] == "C": # scissors
                score += 3

print(score)
