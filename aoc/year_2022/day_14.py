"""Day 14"""

import sys
from typing import Dict, List, Optional, Tuple
from aoc.shared import read_file_lines, Point

lines = read_file_lines("year_2022/input_14.txt")

DEBUG = False


def load_instructions() -> List[List[Point]]:

    output = []
    for line in lines:
        components = line.split(" -> ")
        points = []
        for component in components:
            x, y = map(int, component.split(","))
            points.append(Point(x, y))
        output.append(points)

    return output


def print_sparse_grid(
    grid: Dict[Tuple[int, int], str], sand: Optional[Point] = None
) -> None:

    if not DEBUG:
        return

    min_x = sys.maxsize
    max_x = -sys.maxsize
    min_y = sys.maxsize
    max_y = -sys.maxsize

    keys = list(grid.keys())

    if sand is not None:
        keys.append((sand.x, sand.y))

    for x, y in keys:
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    for y in range(min_y - 2, max_y + 2):
        for x in range(min_x - 2, max_x + 2):
            if sand is not None and sand.x == x and sand.y == y:
                print("s", sep="", end="")
            else:
                print(grid.get((x, y), "."), sep="", end="")
        print()

    print()


def load_grid(floor: bool) -> Tuple[int, Dict[Tuple[int, int], str]]:
    instructions = load_instructions()
    grid = {}

    largest_y = -sys.maxsize

    for instruction in instructions:
        for (p1, p2) in zip(instruction, instruction[1:]):
            if max(p1.y, p2.y) > largest_y:
                largest_y = max(p1.y, p2.y)
            if p1.x == p2.x:
                for y in range(min(p1.y, p2.y), max(p1.y, p2.y) + 1):
                    grid[(p1.x, y)] = "#"
            elif p1.y == p2.y:
                for x in range(min(p1.x, p2.x), max(p1.x, p2.x) + 1):
                    grid[(x, p1.y)] = "#"

    if not floor:
        return largest_y, grid

    # The floor is "infinite", but we can cheat by making sure it's at least
    # twice as wide as the height since a grain of sand can't go more than 45
    # degrees. To avoid off by one errors, we'll just do twice the width on each
    # side.

    for x in range(500 - largest_y * 2, 500 + largest_y * 2):
        grid[(x, largest_y + 2)] = "#"

    return largest_y + 2, grid


def simulate(floor: bool) -> int:
    """Part 1."""

    largest_y, grid = load_grid(floor)
    sand_counter = 0
    hit_abyss = False
    while not hit_abyss:
        sand_counter += 1

        if grid.get((500, 0)) is not None:
            return sand_counter - 1

        sand = Point(500, 0)
        print_sparse_grid(grid, sand)

        while sand is not None:
            if grid.get((sand.x, sand.y + 1)) is None:
                sand = Point(sand.x, sand.y + 1)
            elif grid.get((sand.x - 1, sand.y + 1)) is None:
                sand = Point(sand.x - 1, sand.y + 1)
            elif grid.get((sand.x + 1, sand.y + 1)) is None:
                sand = Point(sand.x + 1, sand.y + 1)
            else:
                grid[(sand.x, sand.y)] = "O"
                sand = None

            print_sparse_grid(grid, sand)

            if sand is not None and sand.y >= largest_y:
                hit_abyss = True
                break

    return sand_counter - 1


def part1() -> int:
    """Part 1."""

    return simulate(floor=False)


def part2() -> int:
    """Part 2."""

    return simulate(floor=True)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
