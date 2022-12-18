from inputs.input import get_input

inp = get_input(18).read().splitlines()

droplets = dict()
air = set()


min_x = 0
max_x = 0
min_y = 0
max_y = 0
min_z = 0
max_z = 0


def is_valid(xyz):
    return (
        (
            xyz in droplets
        )
        or
        (
            (
                xyz not in droplets
            )
            and
            (
                xyz not in air
            )
        )
    )


class Droplet:
    def __init__(self, line):
        self.x, self.y, self.z = map(int, line.split(","))
        droplets[(self.x, self.y, self.z)] = self
        global min_x, max_x, min_y, max_y, min_z, max_z
        if self.x < min_x:
            min_x = self.x
        if self.x > max_x:
            max_x = self.x
        if self.y < min_y:
            min_y = self.y
        if self.y > max_y:
            max_y = self.y
        if self.z < min_z:
            min_z = self.z
        if self.z > max_z:
            max_z = self.z

    def scan(self):
        self.sides = 6
        if is_valid((self.x, self.y, self.z + 1)):
            self.sides -= 1
        if is_valid((self.x, self.y + 1, self.z)):
            self.sides -= 1
        if is_valid((self.x + 1, self.y, self.z)):
            self.sides -= 1
        if is_valid((self.x, self.y, self.z - 1)):
            self.sides -= 1
        if is_valid((self.x, self.y - 1, self.z)):
            self.sides -= 1
        if is_valid((self.x - 1, self.y, self.z)):
            self.sides -= 1
        return self.sides


for line in inp:
    Droplet(line)


air.add((-1, -1, -1))

change = True
while change:
    change = False
    for x in range(min_x-1, max_x + 2):
        for y in range(min_y-1, max_y + 2):
            for z in range(min_z-1, max_z + 2):
                if (x, y, z) in air:
                    if (
                        (x, y, z + 1) not in droplets
                        and (x, y, z + 1) not in air
                    ):
                        air.add((x, y, z + 1))
                        change = True
                    if (
                        (x, y + 1, z) not in droplets
                        and (x, y + 1, z) not in air
                    ):
                        air.add((x, y + 1, z))
                        change = True
                    if (
                        (x + 1, y, z) not in droplets
                        and (x + 1, y, z) not in air
                    ):
                        air.add((x + 1, y, z))
                        change = True
                    if (
                        (x, y, z - 1) not in droplets
                        and (x, y, z - 1) not in air
                    ):
                        air.add((x, y, z - 1))
                        change = True
                    if (
                        (x, y - 1, z) not in droplets
                        and (x, y - 1, z) not in air
                    ):
                        air.add((x, y - 1, z))
                        change = True
                    if (
                        (x - 1, y, z) not in droplets
                        and (x - 1, y, z) not in air
                    ):
                        air.add((x - 1, y, z))
                        change = True

total = 0
for droplet in droplets.values():
    total += droplet.scan()

print(total)
