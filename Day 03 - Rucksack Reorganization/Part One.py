from inputs.input import get_input

inp = get_input(3).read().splitlines()

sum_priorities = 0

for bag in inp:
    size = len(bag)
    c1 = bag[0:int(size/2)]
    c2 = bag[int(size/2):size]
    for item in c1:
        if item in c2:
            n = ord(item)
            if item.islower():
                n -= 96
            else:
                n -= 38
            sum_priorities += n
            break

print(sum_priorities)
