"""Day 7"""

from functools import cache
from aoc.shared import read_file_lines

lines = [list(l) for l in read_file_lines("year_2025/input_07.txt")]


def part1() -> int:
    """Part 1."""

    indices = set([lines[0].index("S")])
    splits = 0

    for row in lines[1:]:
        to_remove: set[int] = set()
        to_add: set[int] = set()
        for index in indices:
            if row[index] == "^":
                to_remove.add(index)
                to_add.add(index - 1)
                to_add.add(index + 1)
                splits += 1
        indices.difference_update(to_remove)
        indices.update(to_add)

    return splits


def part2() -> int:
    """Part 2."""

    @cache
    def solutions(y: int, x: int) -> int:

        if lines[y][x] == "^":
            return solutions(y, x - 1) + solutions(y, x + 1)

        if y == len(lines):
            return 1

        while lines[y + 1][x] != "^":
            y += 1
            if y + 1 >= len(lines):
                return 1

        return solutions(y + 1, x)

    py, px = 0, lines[0].index("S")

    while lines[py][px] != "^":
        py += 1

    return solutions(py, px)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
