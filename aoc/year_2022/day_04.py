"""Day 4"""

from typing import Tuple
from aoc.shared import read_file_lines

lines = read_file_lines("year_2022/input_04.txt")


class Range:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def contains(self, other: "Range") -> bool:
        return other.start >= self.start and other.end <= self.end

    def overlaps(self, other: "Range") -> bool:
        return (other.start <= self.start <= other.end) or (
            self.start <= other.start <= self.end
        )

    @staticmethod
    def from_string(value: str) -> "Range":
        start_str, end_str = value.split("-")
        return Range(int(start_str), int(end_str))


def get_contents() -> Tuple[Range, Range]:
    output = []
    for line in lines:
        r1, r2 = line.split(",")
        output.append((Range.from_string(r1), Range.from_string(r2)))
    return output


def part1() -> int:
    """Part 1."""

    contents = get_contents()

    counter = 0

    for r1, r2 in contents:
        if r1.contains(r2) or r2.contains(r1):
            counter += 1

    return counter


def part2() -> int:
    """Part 2."""

    contents = get_contents()

    counter = 0

    for r1, r2 in contents:
        if r1.overlaps(r2):
            counter += 1

    return counter


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
