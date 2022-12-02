from inputs.input import get_input

inp = get_input(1).read().split("\n\n")

inp = [i.split("\n") for i in inp]

max_sum = 0

for i in inp:
    s = sum((int(j) for j in i))
    if s > max_sum:
        max_sum = s

print(max_sum)
