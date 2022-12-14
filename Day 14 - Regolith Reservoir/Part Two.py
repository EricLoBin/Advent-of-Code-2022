from inputs.input import get_input

inp = [i.split(" -> ") for i in get_input(14).read().splitlines()]


lowest = 0
sand_spawner = (500, 0)
infinite_floor_y = 0

#   -
# - o +
#   +

scan = {}

for rocks in inp:
    for i in range(1, len(rocks)): # ((x1, y1) -> (x2, y2))
        x1, y1 = (int(i) for i in rocks[i-1].split(","))
        x2, y2 = (int(i) for i in rocks[i].split(","))
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                scan[(x1, y)] = "#"
        else:
            for x in range(min(x1, x2), max(x1, x2)+1):
                scan[(x, y1)] = "#"
        low = max(y1, y2)
        if low > lowest:
            lowest = low

# Made for the test input
# def print_scan():
#     for j in range(0, infinite_floor_y + 1):
#         for i in range(490, 510):
#             if j == infinite_floor_y:
#                 print("#", end="")
#             elif (i, j) not in scan:
#                 print(" ", end="")
#             else:
#                 print(scan[(i, j)], end="")
#         print()
####################################
# 498,4 -> 498,6 -> 496,6          #
# 503,4 -> 502,4 -> 502,9 -> 494,9 #
####################################

def spawn_sand():
    x, y = [*sand_spawner]
    while scan.get(sand_spawner) == None:
        if y == infinite_floor_y - 1:
            scan[(x, y)] = "o"
            return True
        elif (x, y+1) not in scan:
            y += 1
        elif (x-1, y+1) not in scan:
            x -= 1
        elif (x+1, y+1) not in scan:
            x += 1
        else:
            scan[(x, y)] = "o"
            return True
    return False

infinite_floor_y = lowest + 2

continue_runinnig = True
count_sand = -1
while continue_runinnig:
    count_sand += 1
    continue_runinnig = spawn_sand()

# print_scan()

print(count_sand)
