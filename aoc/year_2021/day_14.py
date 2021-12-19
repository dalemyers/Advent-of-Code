"""Day 14"""

from collections import defaultdict
from typing import Dict, List, Tuple
from aoc.shared.input import read_file_lines


def get_info(raw_lines: List[str]) -> Tuple[str, Dict[str, str]]:
    template = raw_lines[0]
    insertions = {}
    for line in raw_lines[2:]:
        pattern, insert = line.split(" -> ")
        insertions[pattern] = insert

    return template, insertions


def get_delta(template: str, insertions: Dict[str, str], steps: int) -> int:
    insertion_counts = defaultdict(int)
    counts = defaultdict(int)

    for index in range(0, len(template) - 1):
        pair = template[index] + template[index + 1]
        counts[pair] += 1
        insertion_counts[template[index]] += 1

    insertion_counts[template[-1]] += 1

    for _ in range(steps):
        for (a, b), count in counts.copy().items():
            counts[a + b] -= count
            insertion = insertions[a + b]
            insertion_counts[insertion] += count
            counts[a + insertion] += count
            counts[insertion + b] += count

    max_count = max(insertion_counts.values())
    min_count = min(insertion_counts.values())

    diff = max_count - min_count

    return diff


def part1() -> int:
    """Part 1."""

    raw_lines = read_file_lines("year_2021/input_14.txt")
    template, insertions = get_info(raw_lines)

    return get_delta(template, insertions, 10)


def part2() -> int:
    """Part 2."""

    raw_lines = read_file_lines("year_2021/input_14.txt")
    template, insertions = get_info(raw_lines)

    return get_delta(template, insertions, 40)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
