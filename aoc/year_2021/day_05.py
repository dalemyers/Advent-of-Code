"""Day 5"""

from collections import defaultdict
import re
from typing import Dict, List, Tuple
from aoc.shared import read_file_lines


def get_coordinates() -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    coordinates = []

    for line in read_file_lines("year_2021/input_05.txt"):
        match = re.search(r"([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)", line.strip())
        c = (
            (int(match.group(1)), int(match.group(2))),
            (int(match.group(3)), int(match.group(4))),
        )
        coordinates.append(c)

    return coordinates


def get_visited(
    coordinates: List[Tuple[Tuple[int, int], Tuple[int, int]]], *, diagonal: bool
) -> Dict[int, Dict[int, int]]:
    visited = defaultdict(lambda: defaultdict(int))

    for ((sx, sy), (ex, ey)) in coordinates:
        if sx == ex:
            # Vertical
            for i in range(min(sy, ey), max(sy, ey) + 1):
                visited[i][sx] += 1
        elif sy == ey:
            # Horizontal
            for i in range(min(sx, ex), max(sx, ex) + 1):
                visited[sy][i] += 1
        elif diagonal:
            y_step = 1 if ey > sy else -1
            x_step = 1 if ex > sx else -1

            for y, x in zip(range(sy, ey + y_step, y_step), range(sx, ex + x_step, x_step)):
                visited[y][x] += 1

    return visited


def get_count(visited: Dict[int, Dict[int, int]]) -> int:
    count = 0
    for row in visited.values():
        for value in row.values():
            if value >= 2:
                count += 1

    return count


def part1() -> int:
    """Part 1."""

    coordinates = get_coordinates()

    visited = get_visited(coordinates, diagonal=False)

    return get_count(visited)


def part2() -> int:
    """Part 2."""

    coordinates = get_coordinates()

    visited = get_visited(coordinates, diagonal=True)

    return get_count(visited)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
