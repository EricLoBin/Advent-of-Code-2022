from inputs.input import get_input

inp = get_input(9).read().splitlines()

tail_visited = set()

class ropeKnot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None

    def move(self, prev_x, prev_y):
        # Get distance
        distance = (self.x-prev_x, self.y-prev_y)

        # Does not move
        if (2 not in distance) and (-2 not in distance):
            return

        # Diagonal case (not (2, 2) because it is already handled by the horizontal and vertical case)
        if (distance[0] != 0 and distance[1] != 0) and not (abs(distance[0]) == abs(distance[1]) == 2):
            # Transform diagonal case into horizontal or vertical case
            if abs(distance[0]) < abs(distance[1]):
                self.x -= distance[0]
            else:
                self.y -= distance[1]
            distance = (self.x-prev_x, self.y-prev_y)

        # Horizontal case
        if distance[0] != 0:
            if distance[0] > 0:
                self.x -= 1
            else:
                self.x += 1

        # Vertical case
        if distance[1] != 0:
            if distance[1] > 0:
                self.y -= 1
            else:
                self.y += 1

        # Last knot
        if self.next == None:
            global tail_visited
            tail_visited.add((self.x, self.y))
        else:
            # Move next knot
            self.next.move(self.x, self.y)


head = ropeKnot(0, 0)

nxt = head
for _ in range(9):
    nxt.next = ropeKnot(0, 0)
    nxt = nxt.next

def move_head(direction):
    global head
    if direction == 'U':
        head.y += 1
    elif direction == 'D':
        head.y -= 1
    elif direction == 'R':
        head.x += 1
    elif direction == 'L':
        head.x -= 1
    head.next.move(head.x, head.y)


# show 2d representation
def show():
    knots = [(head.x, head.y)]
    nxt = head.next
    while nxt != None:
        knots.append((nxt.x, nxt.y))
        nxt = nxt.next
    for y in range(4, -1, -1):
        for x in range(6):
            if (x, y) in knots:
                print(knots.index((x, y)), end='')
            else:
                print('.', end='')
        print()
    print()


for line in inp:
    direction, moves = line.split(' ')
    for _ in range(int(moves)):
        move_head(direction)
        # show()

tail_visited.add(()) # add last tail position

print(len(tail_visited))
