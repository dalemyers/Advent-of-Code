"""Day 2"""

from typing import List, Tuple
from aoc.shared import read_file_lines

values = read_file_lines("year_2021/input_03.txt")
WIDTH = len(values[0])


def count_bits(values: str, index: int) -> Tuple[int, int]:
    count_0 = 0
    count_1 = 0
    for value in values:
        if value[index] == "0":
            count_0 += 1
        else:
            count_1 += 1

    return count_0, count_1


def part1() -> int:
    """Part 1."""

    gamma = ""
    epsilon = ""

    for index in range(WIDTH):
        count_0, count_1 = count_bits(values, index)

        if count_0 > count_1:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return int(gamma, base=2) * int(epsilon, base=2)


def get_filtered(values: List[int], largest_ones: bool) -> int:
    filtered = values[:]

    for index in range(WIDTH):
        count_0, count_1 = count_bits(filtered, index)

        new_filter = []

        for value in filtered:
            if count_1 >= count_0:
                if largest_ones and value[index] == "1":
                    new_filter.append(value)
                elif not largest_ones and value[index] == "0":
                    new_filter.append(value)
            else:
                if largest_ones and value[index] == "0":
                    new_filter.append(value)
                elif not largest_ones and value[index] == "1":
                    new_filter.append(value)

        filtered = new_filter

        if len(filtered) == 1:
            break

    return int(filtered[0], base=2)


def part2() -> int:
    """Part 2."""

    o2_rating = get_filtered(values, True)
    co2_rating = get_filtered(values, False)

    return o2_rating * co2_rating


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
