"""Day 4"""

from collections import Counter
from aoc.shared import read_file_lines


grid = [list(l) for l in read_file_lines("year_2025/input_04.txt")]


def get(y: int, x: int) -> int:
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        return 1 if grid[y][x] == "@" else 0
    return 0


def surrounding_count(y: int, x: int) -> int:
    return (
        get(y - 1, x - 1)
        + get(y - 1, x)
        + get(y - 1, x + 1)
        + get(y, x - 1)
        + get(y, x + 1)
        + get(y + 1, x - 1)
        + get(y + 1, x)
        + get(y + 1, x + 1)
    )


def part1() -> int:
    """Part 1."""

    total = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != "@":
                continue
            if surrounding_count(y, x) < 4:
                total += 1

    return total


def part2() -> int:
    """Part 2."""

    total = 0

    while True:
        removals = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] != "@":
                    continue
                if surrounding_count(y, x) < 4:
                    total += 1
                    removals.append((y, x))

        if not removals:
            break

        for y, x in removals:
            grid[y][x] = "."

    return total


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
