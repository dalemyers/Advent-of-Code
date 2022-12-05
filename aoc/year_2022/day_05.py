"""Day 5"""

from typing import List
from aoc.shared import read_file_lines

lines = read_file_lines("year_2022/input_05.txt", strip=False)


class Move:
    def __init__(self, count: int, from_stack: int, to_stack: int) -> None:
        self.count = count
        self.from_stack = from_stack
        self.to_stack = to_stack

    @staticmethod
    def from_entry(entry: str) -> "Move":
        entry = entry.replace("move ", "").replace(" from", "").replace(" to", "")
        values = entry.split(" ")
        return Move(int(values[0]), int(values[1]), int(values[2]))

    def __repr__(self) -> str:
        return f"<Move count={self.count} from={self.from_stack} to={self.to_stack}>"


def parse_stacks(raw: List[str]) -> List[List[str]]:
    stacks = []

    id_line = raw[-1]
    while "  " in id_line:
        id_line = id_line.replace("  ", " ").strip()

    count = len(id_line.split(" "))

    for _ in range(count):
        stacks.append([])

    raw = raw[:-1]
    raw.reverse()

    for line in raw:
        line = line.strip("\n")
        values = []

        for index in range(0, len(line), 4):
            value = line[index : index + 4]
            value = value.replace("[", "").replace("]", "").strip()
            if len(value) == 0:
                values.append(None)
            else:
                values.append(value)

        for value, stack in zip(values, stacks):
            if value is not None:
                stack.append(value)

    return stacks


def load() -> None:
    stacks = []
    moves = []

    current = stacks

    for line in lines:
        if len(line.strip()) == 0:
            current = moves
            continue
        current.append(line)

    parsed_moves = list(map(Move.from_entry, moves))
    parsed_stacks = parse_stacks(stacks)
    return parsed_stacks, parsed_moves


def run(model: int) -> str:
    stacks, moves = load()

    for move in moves:
        from_stack = stacks[move.from_stack - 1]
        to_stack = stacks[move.to_stack - 1]

        if model == 9001:
            to_stack += from_stack[-move.count :]
        else:
            to_stack += reversed(from_stack[-move.count :])

        stacks[move.from_stack - 1] = from_stack[: -move.count]

    output = ""
    for stack in stacks:
        output += stack[-1]

    return output


def part1() -> str:
    """Part 1."""
    return run(9000)


def part2() -> str:
    """Part 2."""

    return run(9001)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
