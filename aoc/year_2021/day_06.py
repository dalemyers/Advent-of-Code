"""Day 6"""

from collections import defaultdict
import re
from typing import Dict, List, Tuple
from aoc.shared import read_int_comma_separated_from_file


def count_fish(fish: List[int], days: int) -> int:
    counts = defaultdict(int)

    for f in fish:
        counts[f] += 1

    for _ in range(days):
        new_counts = defaultdict(int)
        for i in range(0, 9):
            if i == 0:
                new_counts[8] = counts[0]
                new_counts[6] = counts[0]
            elif i == 7:
                new_counts[6] += counts[7]
            else:
                new_counts[i - 1] = counts[i]
        counts = new_counts

    totals = 0

    for count in counts.values():
        totals += count

    return totals


def part1() -> int:
    """Part 1."""

    fish = read_int_comma_separated_from_file("year_2021/input_06.txt")

    return count_fish(fish, 80)


def part2() -> int:
    """Part 2."""

    fish = read_int_comma_separated_from_file("year_2021/input_06.txt")

    return count_fish(fish, 256)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
