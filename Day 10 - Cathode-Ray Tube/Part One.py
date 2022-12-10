from inputs.input import get_input

inp = get_input(10).read().splitlines()

cycle = 0
cycle_goal = 20
x = 1

s = 0

for line in inp:
    cycle += 1
    if cycle  == cycle_goal:
        s += x*cycle
        cycle_goal += 40
    if line == 'noop':
        continue
    cycle += 1
    if cycle == cycle_goal:
        s += x*cycle
        cycle_goal += 40
    x += int(line.split(' ')[1])

    if cycle == 220:
        break

print(s)
