"""Day 1"""

from aoc.shared import read_file_lines

lines = read_file_lines("year_2025/input_01.txt")


def part1() -> int:
    """Part 1."""

    count = 0
    index = 50
    for value in lines:
        direction = value[0]
        distance = int(value[1:])
        if direction == "R":
            index += distance
        else:
            index -= distance
        index %= 100
        if index == 0:
            count += 1
    return count


def part2() -> int:
    """Part 2."""

    count = 0
    index = 50
    for value in lines:
        direction = value[0]
        distance = int(value[1:])
        cycles = distance // 100
        count += cycles
        distance -= cycles * 100
        start_index = index
        if direction == "R":
            index += distance
        else:
            index -= distance
        if index >= 100 or index <= 0:
            index %= 100
            if (index == 0 and distance != 0) or (index != 0 and start_index != 0):
                count += 1
    return count


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
