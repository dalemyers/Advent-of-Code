"""Day 8"""

from typing import Tuple

from aoc.shared import read_int_grid_file


lines = read_int_grid_file("year_2022/input_08.txt")


def view_trees() -> Tuple[int, int]:
    count = 0
    max_scenic_score = 0

    for y, row in enumerate(lines):
        for x, tree in enumerate(row):
            if x == 0 or y == 0 or x + 1 == len(row) or y + 1 == len(lines):
                count += 1
                continue

            slices = []
            slices.append(row[0:x][::-1])
            slices.append(row[x + 1 :])
            slices.append([lines[i][x] for i in range(0, y)][::-1])
            slices.append([lines[i][x] for i in range(y + 1, len(lines))])
            visible = False
            scenic_score = 1

            for s in slices:
                visibility = 0
                for t in s:
                    visibility += 1
                    if t >= tree:
                        break
                scenic_score *= visibility
                if all(t < tree for t in s):
                    visible = True

            max_scenic_score = max(max_scenic_score, scenic_score)

            if visible:
                count += 1

    return count, max_scenic_score


def part1() -> int:
    """Part 1."""

    count, _ = view_trees()
    return count


def part2() -> int:
    """Part 2."""
    _, max_scenic_scorec = view_trees()
    return max_scenic_scorec


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
