"""Day 8"""

from collections import defaultdict
import math

from aoc.shared import read_file_lines

lines = [tuple(map(int, line.split(","))) for line in read_file_lines("year_2025/input_08.txt")]


class Node:

    x: int
    y: int
    z: int
    circuit: int

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.circuit = 0

    def __repr__(self) -> str:
        v = f"Node({self.x}, {self.y}, {self.z}"
        if self.circuit != 0:
            v += f", circuit={self.circuit}"
        v += ")"
        return v

    @staticmethod
    def from_tuple(t: tuple[int, int, int]) -> "Node":
        return Node(t[0], t[1], t[2])

    def distance(self, other: "Node") -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))


def part1() -> int:
    """Part 1."""

    points = [Node.from_tuple(t) for t in lines]
    next_circuit_value = 1

    connections_count = 0

    while connections_count < 10:
        min_distance = -1
        a = Node(0, 0, 0)
        b = Node(0, 0, 0)
        for p1 in points:
            for p2 in points:
                if p1 == p2:
                    continue
                if p1.circuit != 0 and p1.circuit == p2.circuit:
                    continue
                distance = p1.distance(p2)
                if min_distance == -1 or distance < min_distance:
                    min_distance = distance
                    a = p1
                    b = p2

        if a.circuit != 0 and b.circuit != 0:
            # Already in a circuit
            continue

        if a.circuit == 0 and b.circuit == 0:
            a.circuit = next_circuit_value
            b.circuit = next_circuit_value
            next_circuit_value += 1
        elif a.circuit != 0 and b.circuit == 0:
            b.circuit = a.circuit
        elif a.circuit == 0 and b.circuit != 0:
            a.circuit = b.circuit
        else:
            raise ValueError("Unreachable")
        connections_count += 1

        print(f"Connected {a} to {b} with distance {min_distance:.2f}")

    unconnected = set(p for p in points if p.circuit == 0)

    circuits: list[set[Point]] = list(unconnected)

    while True:
        circuit: set[Point] = set()
        first = list(connections.keys())[0]
        circuit.add(first)
        while True:
            added = False
            to_pop: list[Point] = []
            for key in circuit:
                connected_points = connections[key]
                for point in connected_points:
                    if point not in circuit:
                        added = True
                        circuit.add(point)
                        to_pop.append(key)

            for key in to_pop:
                del connections[key]

            if not added:
                break

        if len(circuit) == 0:
            break

        circuits.append(circuit)

    print(len(circuits))


def part2() -> int:
    """Part 2."""

    return 0


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
