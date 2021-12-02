"""Day 2"""

from aoc.shared import read_file_lines

values = read_file_lines("year_2021/input_02.txt")


def part1() -> int:
    """Part 1."""

    h_pos = 0
    depth = 0

    for line in values:
        direction, distance_str = line.split(" ")
        distance = int(distance_str)

        if direction == "forward":
            h_pos += distance
        elif direction == "down":
            depth += distance
        else:
            depth -= distance

    return h_pos * depth


def part2():
    """Part 2."""

    h_pos = 0
    depth = 0
    aim = 0

    for line in values:
        direction, distance_str = line.split(" ")
        distance = int(distance_str)

        if direction == "forward":
            h_pos += distance
            depth += aim * distance
        elif direction == "down":
            aim += distance
        else:
            aim -= distance

    return h_pos * depth


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
