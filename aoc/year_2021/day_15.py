"""Day 15"""

import math
from typing import List

from aoc.shared.grids import get_surrounding_points
from aoc.shared.input import read_int_grid_file


def get_path_cost(grid: List[List[int]]) -> int:

    open_list = set([(0, 0)])
    start_distances = {(0, 0): 0}
    adjacent = {(0, 0): (0, 0)}

    closed = set()

    height = len(grid)
    width = len(grid[0])

    end = (height - 1, width - 1)

    while open_list:

        current = None
        for y, x in open_list:
            if current is None:
                current = (y, x)
                continue

            if start_distances[(y, x)] < start_distances[current]:
                current = (y, x)

        if current == end:
            break

        children = get_surrounding_points(current[0], current[1], grid, height=height, width=width)

        for child in children:
            weight = grid[child[0]][child[1]]
            if child not in open_list and child not in closed:
                open_list.add(child)
                adjacent[child] = current
                start_distances[child] = start_distances[current] + weight
                continue

            if start_distances[child] > start_distances[current] + weight:
                start_distances[child] = start_distances[current] + weight
                adjacent[child] = current

                if child in closed:
                    closed.remove(child)
                    open_list.add(child)

        open_list.remove(current)
        closed.add(current)

    reconst_path = []
    cost = 0

    new_grid = []
    for _ in range(len(grid)):
        new_grid.append([" "] * len(grid[0]))

    while adjacent[current] != current:
        cost += grid[current[0]][current[1]]
        reconst_path.append(current)
        current = adjacent[current]
        new_grid[current[0]][current[1]] = str(grid[current[0]][current[1]])

    reconst_path.append((0, 0))

    reconst_path.reverse()

    return cost


def part1() -> int:
    """Part 1."""

    values = read_int_grid_file("year_2021/input_15.txt")

    cost = get_path_cost(values)

    return cost


def part2() -> int:
    """Part 2."""

    values = read_int_grid_file("year_2021/input_15.txt")

    original_height = len(values)
    original_width = len(values[0])

    for _ in range(4):
        for row in values:
            row.extend((x + 1) if x < 9 else 1 for x in row[-original_height:])

    for _ in range(4):
        for row in values[-original_width:]:
            values.append([(x + 1) if x < 9 else 1 for x in row])

    cost = get_path_cost(values)

    return cost


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
