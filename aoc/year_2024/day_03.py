"""Day 3"""

import re

from aoc.shared import read_file_lines

lines = read_file_lines("year_2024/input_03.txt")
instructions = "".join(lines)


def part1() -> int:
    """Part 1."""
    matches = re.findall(r"mul\((\d+),(\d+)\)", instructions)

    total = 0

    for a, b in matches:
        total += int(a) * int(b)

    return total


def part2() -> int:
    """Part 2."""

    matches = re.findall(r"(?:mul\(\d+,\d+\))|(?:do\(\))|(?:don't\(\))", instructions)

    total = 0
    enabled = True

    for match in matches:
        if match == "don't()":
            enabled = False
            continue

        if match == "do()":
            enabled = True
            continue

        if not enabled:
            continue

        num_str = match[4:-1]
        a_str, b_str = num_str.split(",")
        total += int(a_str) * int(b_str)

    return total


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
