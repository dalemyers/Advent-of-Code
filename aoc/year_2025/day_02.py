"""Day 2"""

from aoc.shared import read_file


ranges = list(map(lambda x: tuple(map(int, x.split("-"))), read_file("year_2025/input_02.txt").split(",")))


def part1() -> int:
    """Part 1."""

    invalid_sum = 0

    for start, end in ranges:
        for value_int in range(start, end + 1):
            value = str(value_int)
            left_half = value[: len(value) // 2]
            right_half = value[len(value) // 2 :]
            if left_half == right_half:
                invalid_sum += value_int

    return invalid_sum


def part2() -> int:
    """Part 2."""

    invalid_sum = 0

    for start, end in ranges:
        for value_int in range(start, end + 1):
            value = str(value_int)
            invalid_values = set()
            for length in range(1, (len(value) // 2) + 1):
                part = value[:length]
                repeated = part * (len(value) // length)
                if repeated == value:
                    invalid_values.add(value_int)
            invalid_sum += sum(invalid_values)

    return invalid_sum


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
