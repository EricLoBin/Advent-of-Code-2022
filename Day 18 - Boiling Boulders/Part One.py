from inputs.input import get_input

inp = get_input(18).read().splitlines()

droplets = dict()

class Droplet:
    def __init__(self, line):
        self.x, self.y, self.z = map(int, line.split(","))
        droplets[(self.x, self.y, self.z)] = self

    def scan(self):
        self.sides = 6
        if (self.x, self.y, self.z + 1) in droplets:
            self.sides -= 1
        if (self.x, self.y + 1, self.z) in droplets:
            self.sides -= 1
        if (self.x + 1, self.y, self.z) in droplets:
            self.sides -= 1
        if (self.x, self.y, self.z - 1) in droplets:
            self.sides -= 1
        if (self.x, self.y - 1, self.z) in droplets:
            self.sides -= 1
        if (self.x - 1, self.y, self.z) in droplets:
            self.sides -= 1
        return self.sides


for line in inp:
    Droplet(line)

total = 0
for droplet in droplets.values():
    total += droplet.scan()

print(total)
