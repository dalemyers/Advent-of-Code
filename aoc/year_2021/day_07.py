"""Day 6"""

import math

from aoc.shared import read_int_comma_separated_from_file, triangular


def part1() -> int:
    """Part 1."""

    positions = read_int_comma_separated_from_file("year_2021/input_07.txt")

    best_fuel = float("inf")

    for i in range(min(positions), max(positions)):
        moves = [math.fabs(p - i) for p in positions]
        best_fuel = min(best_fuel, sum(moves))

    return int(best_fuel)


def part2() -> int:
    """Part 2."""

    positions = read_int_comma_separated_from_file("year_2021/input_07.txt")

    best_fuel = float("inf")

    for i in range(min(positions), max(positions)):
        moves = [triangular(int(math.fabs(p - i))) for p in positions]
        best_fuel = min(best_fuel, sum(moves))

    return best_fuel


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
