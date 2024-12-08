"""Day 5"""

from collections import defaultdict
import enum

from aoc.shared import read_chunked


class Direction(enum.Enum):
    before = "before"
    after = "after"


class Rule:

    value: int
    direction: Direction

    def __init__(self, value: int, direction: Direction) -> None:
        self.value = value
        self.direction = direction

    def __str__(self) -> str:
        return f"Rule<{self.value}, {self.direction}>"

    def __repr__(self) -> str:
        return str(self)


chunks = read_chunked("year_2024/input_05.txt")
ordering_rules_list = list(map(lambda x: (int(x[0]), int(x[1])), map(lambda x: x.split("|"), chunks[0].split("\n"))))
ordering_rules = defaultdict(dict)
for a, b in ordering_rules_list:
    ordering_rules[a][b] = Direction.after
    ordering_rules[b][a] = Direction.before

updated_pages = list(map(lambda x: [int(y) for y in x], map(lambda x: x.split(","), chunks[1].split("\n"))))


def is_in_order(updates: list[int]) -> bool:
    for i, v1 in enumerate(updates):
        for j, v2 in enumerate(updates):
            if i == j:
                continue

            rule = ordering_rules[v1][v2]

            if rule == Direction.before and j < i:
                continue

            if rule == Direction.after and j > i:
                continue

            return False

    return True


def sort_updates(updates: list[int]) -> list[int]:

    updates = updates[:]
    had_changes = True

    while had_changes:
        had_changes = False
        for i in range(0, len(updates) - 1):
            a, b = updates[i], updates[i + 1]
            rule = ordering_rules[a][b]
            if rule == Direction.after:
                continue
            updates[i] = b
            updates[i + 1] = a
            had_changes = True

    return updates


def part1() -> int:
    """Part 1."""

    total = 0
    for updates in updated_pages:
        if is_in_order(updates):
            total += updates[int(len(updates) / 2)]

    return total


def part2() -> int:
    """Part 2."""

    total = 0
    for updates in updated_pages:
        if is_in_order(updates):
            continue

        sorted_updates = sort_updates(updates)
        total += sorted_updates[int(len(sorted_updates) / 2)]

    return total


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
