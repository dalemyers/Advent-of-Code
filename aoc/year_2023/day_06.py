"""Day 6"""

import math

from aoc.shared import read_file_lines, product

lines = read_file_lines("year_2023/input_06.txt")


def get_races() -> list[tuple[int, int]]:
    time_line = lines[0]
    distance_line = lines[1]

    times = [int(n) for n in [t for t in time_line.split(" ") if t.strip() != ""][1:]]
    distances = [int(n) for n in [d for d in distance_line.split(" ") if d.strip() != ""][1:]]

    return list(zip(times, distances))


def part1() -> int:
    """Part 1."""

    races = get_races()
    ways_to_win = []

    for time, distance in races:
        count = 0
        for speed in range(1, time):
            remaining_time = time - speed
            distance_travelled = remaining_time * speed
            if distance_travelled > distance:
                count += 1
        ways_to_win.append(count)

    return product(ways_to_win)


def part2() -> int:
    """Part 2."""
    time = int(lines[0].replace(" ", "").split(":")[-1])
    distance = int(lines[1].replace(" ", "").split(":")[-1])

    r1 = (time + math.sqrt(time**2 - (4 * distance))) / 2
    r2 = (time - math.sqrt(time**2 - (4 * distance))) / 2

    return math.ceil(r1 - r2)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
