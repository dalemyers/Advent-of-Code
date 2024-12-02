"""Day 1"""

import math

from aoc.shared import read_file_lines

lines = read_file_lines("year_2024/input_01.txt")
entries_side_by_side = [list(map(int, filter(lambda x: len(x) > 0, line.split(" ")))) for line in lines]
left = [entry[0] for entry in entries_side_by_side]
right = [entry[1] for entry in entries_side_by_side]


def part1() -> int:
    """Part 1."""

    sleft = sorted(left)
    sright = sorted(right)

    total = 0

    for l, r in zip(sleft, sright):
        diff = int(math.fabs(r - l))
        total += diff

    return total


def part2() -> int:
    """Part 2."""

    total = 0
    for l in left:
        count = 0
        for r in right:
            if l == r:
                count += 1
        total += count * l

    return total


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
