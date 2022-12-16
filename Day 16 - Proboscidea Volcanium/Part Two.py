from inputs.input import get_input

MINUTES = 26

inp = get_input(16).read().splitlines()

valves = {}

for line in inp:
    line = line.split(";")
    name = line[0][6:8]
    flow = int(line[0][23:])
    paths = line[1][24:].split(", ") if line[1][22] == "s" else [line[1][23:]]
    valves[name] = {
        "flow": flow,
        "paths": paths
    }

multiverse = set()

multiverse.add((0, 0, tuple(), ("AA", "AA"))) # Total, flow, open valves, current valves

for i in range(MINUTES):
    new_multiverse = set()
    avg_flow = sum(i[1] for i in multiverse) / len(multiverse)
    for universe in multiverse:
        total, flow, open_valves, current_valves = universe
        if (flow == 0 and i % 5 == 0 and i > 0) or (flow < avg_flow and len(multiverse) > 1000):
            continue
        total += flow
        valve1, valve2 = current_valves
        if valve1 not in open_valves and valves[valve1]["flow"] > 0:
            # open the valve1
            new_open_valves = tuple(sorted([*open_valves, valve1]))
            new_flow = valves[valve1]["flow"] + flow
            for path in valves[valve2]["paths"]:
                new_multiverse.add((total, new_flow, new_open_valves, tuple(sorted([*(path, valve1)]))))
            if valve2 not in new_open_valves and valves[valve2]["flow"] > 0:
                # open the valve2
                new_open_valves2 = tuple(sorted([*new_open_valves, valve2]))
                new_flow2 = valves[valve2]["flow"] + new_flow
                new_multiverse.add((total, new_flow2, new_open_valves2, tuple(sorted([*(valve1, valve2)]))))
        if valve2 not in open_valves and valves[valve2]["flow"] > 0:
            # open the valve2
            new_open_valves = tuple(sorted([*open_valves, valve2]))
            new_flow = valves[valve2]["flow"] + flow
            for path in valves[valve1]["paths"]:
                new_multiverse.add((total, new_flow, new_open_valves, tuple(sorted([*(path, valve2)]))))
        for path in valves[valve1]["paths"]:
            for path2 in valves[valve2]["paths"]:
                new_multiverse.add((total, flow, open_valves, tuple(sorted([*(path, path2)]))))
        # if current_valve not in open_valves and valves[current_valve]["flow"] > 0:
        #     # open the valve
        #     new_open_valves = tuple(sorted([*open_valves, current_valve]))
        #     new_flow = valves[current_valve]["flow"] + flow
        #     new_multiverse.add((total, new_flow, new_open_valves, current_valve))
        # for path in valves[current_valve]["paths"]:
        #     # go to the next valve
        #     new_multiverse.add((total, flow, open_valves, path))
    multiverse = new_multiverse

print(max(i[0] for i in multiverse))
