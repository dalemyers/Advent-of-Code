"""Day 9"""

from typing import Iterable
from aoc.shared import read_file_lines

lines = read_file_lines("year_2023/input_09.txt")
sequences = [list(map(int, line.split(" "))) for line in lines]


def all_zero(sequence: Iterable[int]) -> bool:
    return all(s == 0 for s in sequence)


def get_deltas(sequence: list[int]) -> list[list[int]]:
    deltas = [sequence[:]]
    while True:
        current_delta = []
        for a, b in zip(deltas[-1], deltas[-1][1:]):
            delta = b - a
            current_delta.append(delta)
        if all_zero(current_delta):
            break
        deltas.append(current_delta)
    return deltas


def get_next_positive_value(sequence: list[int]) -> int:
    deltas = get_deltas(sequence)
    add_next = 0
    for delta in reversed(deltas):
        add_next += delta[-1]
    return add_next


def get_next_negative_value(sequence: list[int]) -> int:
    deltas = get_deltas(sequence)
    previous = 0
    for delta in reversed(deltas):
        previous = delta[0] - previous
    return previous


def part1() -> int:
    """Part 1."""

    next_values = []

    for sequence in sequences:
        next_value = get_next_positive_value(sequence)
        next_values.append(next_value)

    return sum(next_values)


def part2() -> int:
    """Part 2."""

    next_values = []

    for sequence in sequences:
        next_value = get_next_negative_value(sequence)
        next_values.append(next_value)

    return sum(next_values)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
