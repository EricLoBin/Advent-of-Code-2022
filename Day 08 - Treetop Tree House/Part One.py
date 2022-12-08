from inputs.input import get_input

inp = get_input(8).read().splitlines()

class Tree:
    def __init__(self, height):
        self.height = height
        self.visible = False

total = len(inp)*len(inp[0])

forest = [[Tree(int(tree)) for tree in row] for row in inp]


for i in range(len(forest)):
    h_ij = -1
    h_ji = -1
    rh_ij = -1
    rh_ji = -1
    for j in range(len(forest)):
        if forest[i][j].height > h_ij:
            h_ij = forest[i][j].height
            forest[i][j].visible = True
        if forest[j][i].height > h_ji:
            h_ji = forest[j][i].height
            forest[j][i].visible = True
        if forest[-(i+1)][-(j+1)].height > rh_ij:
            rh_ij = forest[-(i+1)][-(j+1)].height
            forest[-(i+1)][-(j+1)].visible = True
        if forest[-(j+1)][-(i+1)].height > rh_ji:
            rh_ji = forest[-(j+1)][-(i+1)].height
            forest[-(j+1)][-(i+1)].visible = True


for row in forest:
    for tree in row:
        if not tree.visible:
            total -= 1

print(total)
