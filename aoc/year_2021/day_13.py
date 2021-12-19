"""Day 13"""

from typing import List, Optional, Tuple
from aoc.shared.input import read_file_lines


def get_input() -> Tuple[List[Tuple[int, int]], List[Tuple[str, int]]]:
    raw_lines = read_file_lines("year_2021/input_13.txt")
    dots = []
    folds = []

    for line in raw_lines:
        if len(line.strip()) == 0:
            continue
        elif line.startswith("fold along y="):
            folds.append(("y", int(line[len("fold along y=") :])))
        elif line.startswith("fold along x="):
            folds.append(("x", int(line[len("fold along x=") :])))
        else:
            dots.append(tuple(map(int, line.split(","))))

    return dots, folds


def perform_folds(max_folds: Optional[int]) -> int:

    dots, folds = get_input()
    width = max(dot[0] for dot in dots)
    height = max(dot[1] for dot in dots)
    grid = [["." for x in range(width + 1)] for y in range(height + 1)]

    for dot in dots:
        grid[dot[1]][dot[0]] = "#"

    dot_counts = []

    for fold_count, (axis, value) in enumerate(folds):
        if axis == "y":
            new_grid = []
            for y in range(0, value):
                new_grid.append(grid[y])

            for y in range(value + 1, value * 2 + 1):
                original_y = 2 * value - y
                for x in range(len(grid[y])):
                    if grid[y][x] == "#":
                        new_grid[original_y][x] = "#"

        elif axis == "x":
            new_grid = []
            for y in range(0, len(grid)):
                new_grid.append(grid[y][0:value])

            for y in range(0, len(grid)):
                for x in range(value, len(grid[y])):
                    original_x = 2 * value - x
                    if grid[y][x] == "#":
                        new_grid[y][original_x] = grid[y][x]

        grid = new_grid

        dot_count = 0

        for row in grid:
            for c in row:
                if c == "#":
                    dot_count += 1

        dot_counts.append(dot_count)

        if max_folds and fold_count >= max_folds - 1:
            return dot_counts, grid

    return dot_counts, grid


def part1() -> int:
    """Part 1."""

    dot_counts, _ = perform_folds(1)
    return dot_counts[0]


def part2() -> List[List[str]]:
    """Part 2."""

    _, grid = perform_folds(None)

    return grid


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
