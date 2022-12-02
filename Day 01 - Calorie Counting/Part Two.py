from inputs.input import get_input

inp = get_input(1).read().split("\n\n")

inp = [i.split("\n") for i in inp]

inp = list(map(lambda x: sum((int(j) for j in x)), inp))

sum_max = 0

for _ in range(3):
    m = max(inp)
    sum_max += m
    inp.remove(m)

print(sum_max)
