"""Day 12"""

from collections import deque
from typing import Dict, List, Optional, Tuple
from aoc.shared import read_file_lines

raw_grid = read_file_lines("year_2022/input_12.txt")


def load_grid():
    start = (0, 0)
    end = (0, 0)
    grid = {}
    for y, row in enumerate(raw_grid):
        for x, char in enumerate(row):
            if char == "S":
                start = (x, y)
                grid[(x, y)] = 1
            elif char == "E":
                end = (x, y)
                grid[(x, y)] = 26
            else:
                grid[(x, y)] = ord(char) - 96

    return start, end, len(raw_grid[0]), len(raw_grid), grid


def get_surrounding(
    x: int, y: int, width: int, height: int, grid: Dict[Tuple[int, int], int]
) -> List[Tuple[int, int]]:

    output = []

    if y > 0:
        output.append((x, y - 1))

    if x > 0:
        output.append((x - 1, y))

    if x < width - 1:
        output.append((x + 1, y))

    if y < height - 1:
        output.append((x, y + 1))

    output = [
        (nx, ny)
        for (nx, ny) in output
        if (grid[(x, y)] - grid[(nx, ny)] in (0, 1))
        or (grid[(x, y)] - grid[(nx, ny)] <= -1)
    ]

    return output


def find_route(target: Optional[int] = None) -> int:
    start, end, grid_width, grid_height, grid = load_grid()
    visited = set()
    visited.add(end)
    route = deque()
    route.appendleft((0, end))

    index = 0

    while route:
        index += 1
        distance, (ux, uy) = route.popleft()

        if target is not None and grid[(ux, uy)] == target:
            return distance

        if (ux, uy) == start:
            return distance

        for nx, ny in get_surrounding(ux, uy, grid_width, grid_height, grid):

            if (nx, ny) in visited:
                continue

            route.append((distance + 1, (nx, ny)))
            visited.add((nx, ny))

    return None


def part1() -> int:
    """Part 1."""

    return find_route()


def part2() -> int:
    """Part 2."""
    return find_route(ord("a") - 96)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
