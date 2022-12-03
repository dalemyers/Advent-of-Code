"""Day 12"""

from typing import Dict, List
from collections import Counter, defaultdict
from aoc.shared.input import read_file_lines


def find_routes(
    connections: Dict[str, List[str]],
    location: str,
    visited: List[str],
    two_visits: bool,
):

    next_locations = connections[location]
    routes = []
    for next_location in next_locations:
        if next_location == "start":
            continue

        if next_location == "end":
            routes.append(visited + [next_location])
            continue

        small_visited = [l for l in visited if l.lower() == l]
        small_visit_counts = Counter(small_visited)

        if next_location == next_location.lower():
            if next_location in small_visit_counts:
                if two_visits:
                    if 2 in small_visit_counts.values():
                        continue
                else:
                    continue

        routes.extend(
            find_routes(connections, next_location, visited + [next_location], two_visits)
        )

    return routes


def get_connections():
    values = read_file_lines("year_2021/input_12.txt")

    connections = defaultdict(list)
    for line in values:
        p1, p2 = line.split("-")
        connections[p1].append(p2)
        connections[p2].append(p1)

    return connections


def part1() -> int:
    """Part 1."""

    connections = get_connections()
    routes = find_routes(connections, "start", ["start"], False)
    return len(routes)


def part2() -> int:
    """Part 2."""

    connections = get_connections()
    routes = find_routes(connections, "start", ["start"], True)
    return len(routes)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
