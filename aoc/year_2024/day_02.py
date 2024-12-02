"""Day 2"""

import math

from aoc.shared import read_int_grid_file

grid = read_int_grid_file("year_2024/input_02.txt", spaces=True)


def check_report(report: list[int]) -> bool:
    previous_value = report[0]
    is_safe = True
    if report[0] < report[1]:
        increasing = True
    else:
        increasing = False

    for value in report[1:]:
        if increasing:
            if value <= previous_value:
                is_safe = False
                break
        else:
            if value >= previous_value:
                is_safe = False
                break

        delta = int(math.fabs(value - previous_value))
        if delta not in [0, 1, 2, 3]:
            is_safe = False
            break
        previous_value = value
    return is_safe


def part1() -> int:
    """Part 1."""

    safe_count = 0

    for report in grid:
        if check_report(report):
            safe_count += 1

    return safe_count


def part2() -> int:
    """Part 2."""

    safe_count = 0

    for report in grid:
        if check_report(report):
            safe_count += 1
            continue

        for i in range(len(report)):
            new_report = report[:i] + report[i + 1 :]
            is_safe = check_report(new_report)
            if is_safe:
                safe_count += 1
                break

    return safe_count


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
