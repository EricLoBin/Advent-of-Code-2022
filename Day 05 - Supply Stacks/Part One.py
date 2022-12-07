from inputs.input import get_input

inp = get_input(5).read().split("\n\n")


lines_crates = inp[0].split("\n")

piles = {lines_crates[-1][i]: [] for i in range(1, len(lines_crates[0]), 4)}

for i in range(1, len(lines_crates[0]), 4):
    for line in reversed(lines_crates):
        if (
            line[i] == " "
            or not line[i].isalpha()
        ):
            continue
        piles[lines_crates[-1][i]].append(line[i])

instructions = inp[1].split("\n")

for instruction in instructions:
    i = instruction.split(" ")
    quatity = int(i[1])
    pile = i[3]
    destination = i[5]

    for _ in range(quatity):
        piles[destination].append(piles[pile].pop())

for pile in piles:
    print(piles[pile].pop(), end="")

print()
