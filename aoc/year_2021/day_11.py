"""Day 11"""

from typing import List, Optional
from aoc.shared.grids import get_surrounding_points
from aoc.shared.input import read_int_grid_file


def get_values(values: List[List[int]], max_step: Optional[int]):

    total_flashes = 0
    step = 0

    while True:
        step += 1

        flashed = []

        for y in range(len(values)):
            for x in range(len(values)):
                if values[y][x] < 9:
                    values[y][x] += 1
                else:
                    values[y][x] = 0
                    total_flashes += 1
                    flashed.append((y, x))

        while len(flashed) > 0:
            y, x = flashed.pop(0)
            surrounding = get_surrounding_points(y, x, values, diagonals=True)
            for sy, sx in surrounding:
                if values[sy][sx] == 0:
                    continue
                elif values[sy][sx] < 9:
                    values[sy][sx] += 1
                else:
                    values[sy][sx] = 0
                    total_flashes += 1
                    flashed.append((sy, sx))

        all_flashed = True
        for row in values:
            all_flashed = all_flashed and all(v == 0 for v in row)

        if all_flashed or step == max_step:
            return total_flashes, step


def part1() -> int:
    """Part 1."""

    values = read_int_grid_file("year_2021/input_11.txt")
    flashes, _ = get_values(values, 100)

    return flashes


def part2() -> int:
    """Part 2."""

    values = read_int_grid_file("year_2021/input_11.txt")
    _, step = get_values(values, None)

    return step


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
