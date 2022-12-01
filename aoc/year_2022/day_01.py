"""Day 1"""

from aoc.shared import read_chunked_ints

values = read_chunked_ints("year_2022/input_01.txt")


def part1() -> int:
    """Part 1."""

    max_elf = 0

    for elf in values:
        total = sum(elf)
        if total > max_elf:
            max_elf = total

    return max_elf


def part2() -> int:
    """Part 2."""

    max_elves = [0, 0, 0]

    for elf in values:
        total = sum(elf)
        if total > max_elves[-1]:
            max_elves = max_elves[:2] + [total]
            max_elves = sorted(max_elves, reverse=True)

    return sum(max_elves)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
