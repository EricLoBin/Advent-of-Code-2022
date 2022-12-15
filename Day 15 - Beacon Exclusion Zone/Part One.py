from inputs.input import get_input

inp = get_input(15).read().splitlines()

SCAN_Y = 2000000


min_x = float("inf")
max_x = float("-inf")


sensors = {}
beacons_in_scan_y = {}
for line in inp:
    _, _, sensor_x, sensor_y, _, _, _, _, beacon_x, beacon_y = line.split(" ")
    sensor_x = int(sensor_x[2:-1])
    sensor_y = int(sensor_y[2:-1])
    beacon_x = int(beacon_x[2:-1])
    beacon_y = int(beacon_y[2:])

    if min(sensor_x, beacon_x) < min_x:
        min_x = min(sensor_x, beacon_x)
    if max(sensor_x, beacon_x) > max_x:
        max_x = max(sensor_x, beacon_x)

    dx = sensor_x - beacon_x
    dy = sensor_y - beacon_y
    # Faster abs
    if dx < 0:
        dx = -dx
    if dy < 0:
        dy = -dy
    distance_to_point = dx + dy

    sensors[(sensor_x, sensor_y)] = distance_to_point
    if beacon_y == SCAN_Y:
        beacons_in_scan_y[beacon_x] = 1

count = 0

for x in range(min_x, max_x + 1):
    if x % 100000 == 0:
        print(x, "/", max_x, "=", count)
    for point, distance in sensors.items():
        dx = point[0] - x
        dy = point[1] - SCAN_Y
        # Faster abs
        if dx < 0:
            dx = -dx
        if dy < 0:
            dy = -dy

        distance_to_point = dx + dy
        if distance_to_point <= distance:
            count += 1
            break

# get out of bounds points
p = min_x - 1
condition = True
while condition:
    condition = False
    for point, distance in sensors.items():
        dx = point[0] - p
        dy = point[1] - SCAN_Y
        # Faster abs
        if dx < 0:
            dx = -dx
        if dy < 0:
            dy = -dy

        distance_to_point = dx + dy
        if distance_to_point <= distance:
            count += 1
            condition = True
            break
    p -= 1

p = max_x + 1
condition = True
while condition:
    condition = False
    for point, distance in sensors.items():
        dx = point[0] - p
        dy = point[1] - SCAN_Y
        # Faster abs
        if dx < 0:
            dx = -dx
        if dy < 0:
            dy = -dy

        distance_to_point = dx + dy
        if distance_to_point <= distance:
            count += 1
            condition = True
            break
    p += 1


print(count - sum(beacons_in_scan_y.values()))
