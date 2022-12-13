from inputs.input import get_input

start = None
end = None

inp = get_input(12).read().split("\n")

height_map = {}

for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == "E":
            start = (i, j)
            height_map[(i, j)] = {
                "height": ord("z"),
                "moves_to_reach": 0
            }
            continue
        height_map[(i, j)] = {
            "height": ord(inp[i][j]),
            "moves_to_reach": float("inf")
        }

def scan(layer):
    for point, data in height_map.items():
        if data["moves_to_reach"] != layer:
            continue
        for move in [
            height_map.get((point[0]-1, point[1]), None),
            height_map.get((point[0], point[1]-1), None),
            height_map.get((point[0]+1, point[1]), None),
            height_map.get((point[0], point[1]+1), None)
        ]:
            if move != None:
                if data["height"] - move["height"] <= 1:
                    if move["moves_to_reach"] > data["moves_to_reach"]+1:
                        move["moves_to_reach"] = data["moves_to_reach"]+1

height_map[start]["moves_to_reach"] = 0

layer = 0
while len([i for i in height_map.values() if i["height"] == ord("a") and i["moves_to_reach"] != float("inf")]) == 0:
    scan(layer)
    layer += 1

print([i for i in height_map.values() if i["height"] == ord("a") and i["moves_to_reach"] != float("inf")][0]["moves_to_reach"])
