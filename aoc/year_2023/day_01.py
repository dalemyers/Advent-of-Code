"""Day 1"""

from aoc.shared import read_file_lines
from aoc.shared.strings import findall

lines = read_file_lines("year_2023/input_01.txt")


def part1() -> int:
    """Part 1."""

    total = 0
    for line in lines:
        digits = [c for c in line if c.isdigit()]
        total += int(digits[0] + digits[-1])

    return total


def part2() -> int:
    """Part 2."""

    number_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    numbers = list(number_map.keys()) + list(number_map.values())

    total = 0
    for line in lines:
        digits = []
        for number in numbers:
            indices = findall(line, number)
            if len(indices) == 0:
                continue
            digits += [(number, i) for i in indices]

        ordered_digits = sorted(digits, key=lambda t: t[1])
        first_digit = ordered_digits[0][0]
        first_digit = number_map.get(first_digit, first_digit)
        last_digit = ordered_digits[-1][0]
        last_digit = number_map.get(last_digit, last_digit)

        total += int(first_digit + last_digit)

    return total


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
