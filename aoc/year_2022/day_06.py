"""Day 6"""

from aoc.shared import read_file_lines

lines = read_file_lines("year_2022/input_06.txt")


def get_marker_position(data: str, length: int) -> int:
    for i in range(0, len(data)):
        chars = data[i : i + length]
        char_set = set(chars)
        if len(char_set) == length:
            return i + length

    return 0


def part1() -> int:
    """Part 1."""
    line = lines[0]
    return get_marker_position(line, 4)


def part2() -> str:
    """Part 2."""

    line = lines[0]
    return get_marker_position(line, 14)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
