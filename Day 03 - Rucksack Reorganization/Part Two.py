from inputs.input import get_input

inp = get_input(3).read().splitlines()

sum_priorities = 0

for three_bags in range(0, len(inp), 3):
    for item in inp[three_bags]:
        if item in inp[three_bags + 1] and item in inp[three_bags + 2]:
            n = ord(item)
            if item.islower():
                n -= 96
            else:
                n -= 38
            sum_priorities += n
            break

print(sum_priorities)
