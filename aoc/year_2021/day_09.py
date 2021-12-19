"""Day 9"""

from math import prod
from typing import List, Tuple
from aoc.shared.input import read_int_grid_file


def get_value(y: int, x: int, heightmap: List[List[int]]) -> int:
    default = 10
    if y < 0:
        return default
    if y >= len(heightmap):
        return default
    row = heightmap[y]
    if x < 0:
        return default
    if x >= len(row):
        return default
    return row[x]


def get_surrounding_basin_points(
    y: int, x: int, heightmap: List[List[int]]
) -> List[Tuple[int, int]]:
    surrounding = []
    if get_value(y - 1, x, heightmap) < 9:
        surrounding.append((y - 1, x))
    if get_value(y + 1, x, heightmap) < 9:
        surrounding.append((y + 1, x))
    if get_value(y, x - 1, heightmap) < 9:
        surrounding.append((y, x - 1))
    if get_value(y, x + 1, heightmap) < 9:
        surrounding.append((y, x + 1))
    return surrounding


def get_low_points(heightmap: List[List[int]]) -> List[Tuple[int, int]]:
    low_points = []

    for y in range(0, len(heightmap)):
        for x in range(0, len(heightmap[y])):
            upper = get_value(y - 1, x, heightmap)
            lower = get_value(y + 1, x, heightmap)
            left = get_value(y, x - 1, heightmap)
            right = get_value(y, x + 1, heightmap)
            v = heightmap[y][x]
            if v < upper and v < lower and v < left and v < right:
                low_points.append((y, x))

    return low_points


def part1() -> int:
    """Part 1."""

    heightmap = read_int_grid_file("year_2021/input_09.txt")
    low_points = get_low_points(heightmap)

    return sum(heightmap[y][x] + 1 for (y, x) in low_points)


def part2() -> int:
    """Part 2."""

    heightmap = read_int_grid_file("year_2021/input_09.txt")
    low_points = get_low_points(heightmap)

    basin_sizes = []

    for y, x in low_points:
        extend_points = [(y, x)]
        heightmap[y][x] = 10
        basin_size = 1

        while len(extend_points) > 0:
            point = extend_points.pop(0)
            surrounding = get_surrounding_basin_points(point[0], point[1], heightmap)

            for sy, sx in surrounding:
                basin_size += 1
                heightmap[sy][sx] = 10
                extend_points.append((sy, sx))

        basin_sizes.append(basin_size)

    basin_sizes.sort()

    return prod(basin_sizes[-3:])


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
