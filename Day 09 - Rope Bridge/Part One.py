from inputs.input import get_input

inp = get_input(9).read().splitlines()

head = [0, 0]
tail = [0, 0]

tail_visited = set()

def move_tail():
    global tail
    global tail_visited
    tail_visited.add((tail[0], tail[1]))
    distance = (tail[0]-head[0], tail[1]-head[1])

    # Does not move
    if (2 not in distance) and (-2 not in distance):
        return

    # Diagonal case
    if distance[0] != 0 and distance[1] != 0:
        # Transform diagonal case into horizontal or vertical case
        if abs(distance[0]) < abs(distance[1]):
            tail[0] -= distance[0]
        else:
            tail[1] -= distance[1]
        distance = (tail[0]-head[0], tail[1]-head[1])

    # Horizontal case
    if distance[0] != 0:
        if distance[0] > 0:
            tail[0] -= 1
        else:
            tail[0] += 1
        return

    # Vertical case
    if distance[1] != 0:
        if distance[1] > 0:
            tail[1] -= 1
        else:
            tail[1] += 1
        return


def move_head(direction):
    global head
    if direction == 'U':
        head[1] += 1
    elif direction == 'D':
        head[1] -= 1
    elif direction == 'R':
        head[0] += 1
    elif direction == 'L':
        head[0] -= 1


# show 2d representation
def show():
    for y in range(-10, 11):
        for x in range(-5, 11):
            if [x, y] == head:
                print('H', end='')
            elif [x, y] == tail:
                print('T', end='')
            elif (x, y) in tail_visited:
                print('X', end='')
            else:
                print('.', end='')
        print()
    print()


for line in inp:
    direction, moves = line.split(' ')
    for _ in range(int(moves)):
        move_head(direction)
        move_tail()

tail_visited.add((tail[0], tail[1])) # add last tail position

print(len(tail_visited))
