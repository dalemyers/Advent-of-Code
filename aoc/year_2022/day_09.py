"""Day 9"""

import math
from typing import List
from aoc.shared import read_file_lines, Point


lines = read_file_lines("year_2022/input_09.txt")

DEBUG = False


def print_grid(knots: List[Point]) -> None:
    for y in range(15, -15, -1):
        for x in range(-15, 15):
            printed = False

            for index, knot in enumerate(knots):
                if knot.x == x and knot.y == y:
                    if index == 0:
                        print("H", end="")
                    elif index == len(knots):
                        print("T", end="")
                    else:
                        print(index, end="")
                    printed = True
                    break

            if not printed:
                if x == 0 and y == 0:
                    print("s", end="")
                else:
                    print(".", end="")
        print("")
    print()


def simulate_rope(count: int):
    knots = []
    for _ in range(count):
        knots.append(Point(0, 0))

    if DEBUG:
        print_grid(knots)

    visited = set()

    for line in lines:
        direction, count_str = line.split(" ")
        count = int(count_str)

        for _ in range(count):
            if direction == "U":
                knots[0].y += 1
            elif direction == "D":
                knots[0].y -= 1
            elif direction == "R":
                knots[0].x += 1
            else:
                knots[0].x -= 1

            for index, tail in enumerate(knots):
                if index == 0:
                    continue

                previous = knots[index - 1]
                distance = tail.distance(previous)

                if distance - 0.0000001 < math.sqrt(2):
                    break

                delta = (previous - tail).as_sign_only()

                tail += delta

                if DEBUG:
                    print_grid(knots)

            visited.add((knots[-1].x, knots[-1].y))

            if DEBUG:
                print_grid(knots)

    return len(visited)


def part1() -> int:
    """Part 1."""
    return simulate_rope(2)


def part2() -> int:
    """Part 2."""
    return simulate_rope(10)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
