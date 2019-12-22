import math
from typing import List

with open("year_2019/input_10.txt") as input_file:
    contents = input_file.read()


def load_grid(contents) -> List[List[int]]:
    grid = []

    for line in contents.split("\n"):
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
            points_in_angle[theta].append((h, w))

    return len(points_in_angle)


grid = load_grid(contents)

def get_max_detections_location(grid):
    max_detections = 0
    grid_location = None

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == 0:
                continue
            count = detections(grid, x, y)
            if count > max_detections:
                max_detections = count
                grid_location = (x, y)

    return grid_location, max_detections

print("Part 1:", get_max_detections_location(grid))