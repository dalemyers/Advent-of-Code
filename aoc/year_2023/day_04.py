"""Day 4"""

from collections import defaultdict
from aoc.shared import read_file_lines

lines = read_file_lines("year_2023/input_04.txt")

Card = tuple[int, list[int], list[int]]


def read_cards() -> Card:
    output = []
    for line in lines:
        identifier_str, numbers = line.split(":")
        identifier = int(identifier_str.split(" ")[-1].strip())
        winning_numbers_str, my_numbers_str = numbers.split(" | ")
        winning_numbers_str = winning_numbers_str.strip()
        my_numbers_str = my_numbers_str.strip()
        winning_numbers = [int(n) for n in winning_numbers_str.split(" ") if n.strip()]
        my_numbers = [int(n) for n in my_numbers_str.split(" ") if n.strip()]
        output.append((identifier, winning_numbers, my_numbers))
    return output


def part1() -> int:
    """Part 1."""

    cards = read_cards()
    total = 0
    for _, winning_numbers, my_numbers in cards:
        matches = len(set(winning_numbers) & set(my_numbers))
        if matches == 0:
            continue
        points = 2 ** (matches - 1)
        total += points

    return total


def part2() -> int:
    """Part 2."""

    cards = read_cards()
    multipliers = {}

    for i in range(1, len(cards) + 1):
        multipliers[i] = 1

    for index, winning_numbers, my_numbers in cards:
        matches = len(set(winning_numbers) & set(my_numbers))
        if matches == 0:
            continue
        for _ in range(0, multipliers[index]):
            for i in range(index + 1, index + matches + 1):
                if i > len(cards):
                    continue
                multipliers[i] += 1

    return sum(multipliers.values())


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
