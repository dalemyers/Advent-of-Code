import enum
import operator
from typing import Callable, Dict, List, Set, Tuple

class Direction(enum.Enum):
    up = "U"
    down = "D"
    left = "L"
    right = "R"

    def operation(self) -> Callable:
        if self in [Direction.up, Direction.right]:
            return operator.add
        elif self in [Direction.down, Direction.left]:
            return operator.sub

class Instruction:

    direction: Direction
    distance: int

    def __init__(self, instruction: str) -> None:
        self.direction = Direction(instruction[0])
        self.distance = int(instruction[1:])

    def __repr__(self) -> str:
        return f"{self.direction.value}{self.distance}"

def parse_line(line: str) -> List[Instruction]:
    instructions = line.strip().split(",")
    return list(map(Instruction, instructions))


with open("2019/03/input.txt") as f:
    lines = f.readlines()
    wire1_data = parse_line(lines[0])
    wire2_data = parse_line(lines[1])

locations = {}

for identifier, wire in enumerate([wire1_data, wire2_data]):
    x = 0
    y = 0

    if locations.get("0/0") is None:
        locations["0/0"] = set()
    locations["0/0"].add(identifier + 1)

    for instruction in wire:
        step = 1 if instruction.direction in [Direction.up, Direction.right] else -1
        delta = step * instruction.distance

        if instruction.direction in [Direction.up, Direction.down]:
            for value in range(y + step, y + delta + step, step):
                key = f"{x}/{value}"
                if locations.get(key) is None:
                    locations[key] = set()
                locations[key].add(identifier + 1)
            y += delta

        if instruction.direction in [Direction.left, Direction.right]:
            for value in range(x + step, x + delta + step, step):
                key = f"{value}/{y}"
                if locations.get(key) is None:
                    locations[key] = set()
                locations[key].add(identifier + 1)
            x += delta

distances = []

for key, value in locations.items():
    if len(value) <= 1:
        continue

    x_str, y_str = key.split("/")
    x ,y = int(x_str), int(y_str)

    if x == 0 and y == 0:
        continue

    distance = abs(x) + abs(y)
    print(key, distance)
    distances.append(distance)

distances.sort()
print(distances[0])