from inputs.input import get_input

inp = get_input(8).read().splitlines()

class Tree:
    def __init__(self, height):
        self.height = height
        self.score = 0

forest = [[Tree(int(tree)) for tree in row] for row in inp]


for i in range(1, len(forest)-1):
    for j in range(1, len(forest)-1):
        height = forest[i][j].height

        # Left
        l = 0
        for k in range(j-1, -1, -1):
            l += 1
            if forest[i][k].height >= height:
                break

        # Up
        u = 0
        for k in range(i-1, -1, -1):
            u += 1
            if forest[k][j].height >= height:
                break

        # Right
        r = 0
        for k in range(j+1, len(forest)):
            r += 1
            if forest[i][k].height >= height:
                break

        # Down
        d = 0
        for k in range(i+1, len(forest)):
            d += 1
            if forest[k][j].height >= height:
                break

        forest[i][j].score = l * u * r * d

hs = 0
for row in forest:
    for tree in row:
        if tree.score > hs:
            hs = tree.score

print(hs)
