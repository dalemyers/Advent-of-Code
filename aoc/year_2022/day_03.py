"""Day 3"""

from typing import Tuple
from aoc.shared import read_file_lines, group_into

lines = read_file_lines("year_2022/input_03.txt")


def get_contents() -> Tuple[str, str]:
    output = []
    for line in lines:
        length = int(len(line) / 2)
        output.append((line[:length], line[length:]))
    return output


def priority(item: str) -> int:
    if item.isupper():
        return ord(item) - ord("A") + 27

    return ord(item) - ord("a") + 1


def part1() -> int:
    """Part 1."""

    contents = get_contents()
    total_priorities = 0

    for one, two in contents:
        both = list(set(one) & set(two))[0]
        total_priorities += priority(both)

    return total_priorities


def part2() -> int:
    """Part 2."""

    contents = get_contents()
    groups = group_into(3, contents)

    total_priorities = 0

    for e1, e2, e3 in groups:
        in_all = list(set(e1[0] + e1[1]) & set(e2[0] + e2[1]) & set(e3[0] + e3[1]))[0]
        total_priorities += priority(in_all)

    return total_priorities


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
