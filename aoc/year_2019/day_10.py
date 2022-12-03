import math
from typing import List

with open("year_2019/input_10.txt", encoding="utf-8") as input_file:
    contents = input_file.read()


def load_grid(grid_contents) -> List[List[int]]:
    grid = []

    for line in grid_contents.split("\n"):
        row = []
        for character in line:
            if character == "#":
                row.append(1)
            else:
                row.append(0)
        grid.append(row)

    return grid


def detections(grid, x, y) -> int:

    points_in_angle = {}

    for h, row in enumerate(grid):
        for w, value in enumerate(row):
            if value == 0:
                continue
            if h == y and w == x:
                continue
            delta_x = w - x
            delta_y = h - y
            theta = math.atan2(delta_y, delta_x)
            if theta not in points_in_angle:
                points_in_angle[theta] = []
            points_in_angle[theta].append((w, h))

    return points_in_angle


def get_max_detections_location(grid):
    max_detections = 0
    grid_location = None

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == 0:
                continue
            count = len(detections(grid, x, y))
            if count > max_detections:
                max_detections = count
                grid_location = (x, y)

    return grid_location, max_detections


def distance(a, b, x, y) -> float:
    c_2 = math.pow(a - x, 2) + math.pow(b - y, 2)
    return math.sqrt(c_2)


def vaporize(grid, location):
    X, Y = location

    locations = detections(grid, X, Y)

    angles = list(locations.keys())
    angles.sort()

    for index, angle in enumerate(angles):
        if angle >= -math.pi / 2.0:
            angles = angles[index:] + angles[:index]
            break

    for angle in angles:
        locations[angle].sort(key=lambda t: distance(t[0], t[1], X, Y))

    counter = 0
    while True:
        for angle in angles:
            try:
                asteroid = locations.get(angle, []).pop(0)
                counter += 1
            except IndexError:
                continue
            if counter == 200:
                return asteroid


main_grid = load_grid(contents)
detection_location, detection_count = get_max_detections_location(main_grid)
print("Part 1:", detection_location, detection_count)
print("Part 2:", vaporize(main_grid, detection_location))
