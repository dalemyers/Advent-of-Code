"""Day 8"""

import math
from aoc.shared import read_file_lines

lines = read_file_lines("year_2023/input_08.txt")


class DirectionStream:
    def __init__(self, instructions: str) -> None:
        self.index = -1
        self.instructions = instructions

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.instructions):
            self.index = 0
        return self.index, self.instructions[self.index]


def get_data():
    directions = lines[0]

    steps = {}
    for line in lines[2:]:
        source, dests = line.split(" = (")
        dests = dests.replace(")", "").split(", ")
        steps[source] = dests

    return directions, steps


def part1() -> int:
    """Part 1."""

    directions, stepmap = get_data()
    steps = 0

    current = "AAA"
    for _, direction in DirectionStream(directions):
        steps += 1
        current = stepmap[current][0 if direction == "L" else 1]
        if current == "ZZZ":
            break

    return steps


def part2() -> int:
    """Part 2."""

    directions, stepmap = get_data()

    nodes = []
    visits = []

    for node in stepmap.keys():
        if node.endswith("A"):
            nodes.append(node)

    for i, node in enumerate(nodes):
        steps = 0
        visited = set([(-1, node)])
        visits.append([(-1, node)])
        for direction_index, direction in DirectionStream(directions):
            steps += 1
            new = stepmap[nodes[i]][0 if direction == "L" else 1]
            nodes[i] = new
            visits[i].append((direction_index, new))

            if (direction_index, new) in visited:
                break

            visited.add((direction_index, new))

    reduced_visits = []
    for visit_list in visits:
        loop_point = visit_list[-1]
        start_point = visit_list.index(loop_point)

        reduced_visits.append(len(visit_list) - 1 - start_point)

    return math.lcm(*reduced_visits)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
