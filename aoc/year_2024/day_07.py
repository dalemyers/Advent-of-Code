"""Day 7"""

from itertools import combinations_with_replacement

from aoc.shared import read_file_lines

lines = list(map(lambda x: x.split(":"), read_file_lines("year_2024/input_07.txt")))
lines = [(int(x[0]), list(map(int, x[1].strip().split(" ")))) for x in lines]


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


OPERATORS = [add, multiply]


def part1() -> int:
    """Part 1."""

    for result, values in lines:
        operator_length = len(values) - 1
        pairs = list(zip(values, values[1:]))
        operator_perms = list(combinations_with_replacement(OPERATORS, operator_length))

        for op_seq in operator_perms:
            for i in range(0, len(values) - 1):
                operator = op_seq[i]
                values[i + 1] = operator(values[i], values[i + 1])
            if values[-1] == result:
                print("Found:", values[-1])

    return 0


def part2() -> int:
    """Part 2."""

    return 0


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
