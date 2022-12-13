from inputs.input import get_input

start = None
end = None

inp = get_input(12).read().split("\n")

height_map = {}

for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == "S":
            start = (i, j)
            height_map[(i, j)] = {
                "height": ord("a"),
                "moves_to_reach": float("inf")
            }
            continue
        elif inp[i][j] == "E":
            end = (i, j)
            height_map[(i, j)] = {
                "height": ord("z"),
                "moves_to_reach": float("inf")
            }
            continue
        height_map[(i, j)] = {
            "height": ord(inp[i][j]),
            "moves_to_reach": float("inf")
        }

def scan():
    for point, data in height_map.items():
        for move in [
            height_map.get((point[0]-1, point[1]), None),
            height_map.get((point[0], point[1]-1), None),
            height_map.get((point[0]+1, point[1]), None),
            height_map.get((point[0], point[1]+1), None)
        ]:
            if move != None:
                if move["height"] - data["height"] <= 1:
                    if move["moves_to_reach"] > data["moves_to_reach"]+1:
                        move["moves_to_reach"] = data["moves_to_reach"]+1

height_map[start]["moves_to_reach"] = 0

while height_map[end]["moves_to_reach"] == float("inf"):
    scan()

print(height_map[end]["moves_to_reach"])
