from inputs.input import get_input

inp = get_input(10).read().splitlines()

cycle = 0
cycle_goal = 40
x = 1

s = 0

l = [[]]

def write_crt():
    global l
    if (x == len(l[-1])) or (x-1 == len(l[-1])) or (x+1 == len(l[-1])):
        l[-1].append("#")
    else:
        l[-1].append(".")

for line in inp:
    cycle += 1
    write_crt()
    if cycle  == cycle_goal:
        s += x*cycle
        cycle_goal += 40
        l.append([])
    if line == 'noop':
        continue
    cycle += 1
    write_crt()
    if cycle == cycle_goal:
        s += x*cycle
        cycle_goal += 40
        l.append([])
    x += int(line.split(' ')[1])

    if cycle == 240:
        break

for i in l:
    print(''.join(i))
