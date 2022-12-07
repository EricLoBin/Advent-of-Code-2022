from inputs.input import get_input

inp = get_input(4).read().splitlines()

count = 0

for line in inp:
    l = line.split(",")
    r1 = [int(i) for i in l[0].split("-")]
    r2 = [int(i) for i in l[1].split("-")]


    if (
        r1[0] in range(r2[0], r2[1]+1)
        or r1[1] in range(r2[0], r2[1]+1)
        or r2[0] in range(r1[0], r1[1]+1)
        or r2[1] in range(r1[0], r1[1]+1)
    ):
        count += 1

print(count)
