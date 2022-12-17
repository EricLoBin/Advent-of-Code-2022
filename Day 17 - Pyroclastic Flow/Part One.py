from inputs.input import get_input

ROCKS_COUNT = 2022

rocks = [
    {
        (0, 0), (1, 0), (2, 0), (3, 0)
    },
    {
                (1, 2),
        (0, 1), (1, 1), (2, 1),
                (1, 0)
    },
    {
                        (2, 2),
                        (2, 1),
        (0, 0), (1, 0), (2, 0)
    },
    {
        (0, 3),
        (0, 2),
        (0, 1),
        (0, 0)
    },
    {
        (0, 1), (1, 1),
        (0, 0), (1, 0)
    }
]

inp = get_input(17).read()


def can_fall(rock_pos, rock):
    new_position = (rock_pos[0], rock_pos[1] - 1)
    for pos in rock:
        new_pos = (pos[0] + new_position[0], pos[1] + new_position[1])
        pass
        if new_pos in cave or new_pos[1] == -1:
            return False
    return True


char_n = 0
def gas_jet(rock_pos):
    global char_n
    # Jet of hot gas
    new_rock_pos = (
        rock_pos[0] + (1 if inp[char_n] == '>' else -1),
        rock_pos[1]
    )
    char_n += 1
    if char_n >= len(inp): char_n = 0
    # check invalid position
    max_x = max([i[0] + new_rock_pos[0] for i in rock])
    min_x = min([i[0] + new_rock_pos[0] for i in rock])
    if (0 > min_x or max_x > 6):
        new_rock_pos = rock_pos
    for pos in rock:
        new_pos = (pos[0] + new_rock_pos[0], pos[1] + new_rock_pos[1])
        if new_pos in cave:
            new_rock_pos = rock_pos
    return new_rock_pos


def fall(rock_pos):
    # fall
    new_pos = (rock_pos[0], rock_pos[1] - 1)
    return new_pos


spawn_position = (2, 3)

cave = set()

max_y = 0
rock_n = -1
for _ in range(ROCKS_COUNT):
    # new rock
    rock_n += 1
    if rock_n >= len(rocks): rock_n = 0
    rock = rocks[rock_n]
    rock_pos = spawn_position

    rock_pos = gas_jet(rock_pos)
    while can_fall(rock_pos, rock):
        rock_pos = fall(rock_pos)
        rock_pos = gas_jet(rock_pos)

    # add rock to cave
    for pos in rock:
        new_pos = (pos[0] + rock_pos[0], pos[1] + rock_pos[1])
        cave.add(new_pos)
        if new_pos[1] > max_y:
            max_y = new_pos[1]
    spawn_position = (spawn_position[0], max_y + 4)


# print
# for y in range(max_y + 1, -1, -1):
#     for x in range(7):
#         if (x, y) in cave:
#             print('#', end='')
#         else:
#             print('.', end='')
#     print()


print(max_y+1)
