"""Day 10"""

from typing import List, Tuple
from aoc.shared.input import read_file_lines


def filter_lines(lines: List[str]) -> Tuple[List[str], List[str]]:

    stacks = []
    corrupted_lines = []

    for line in lines:
        stack = []
        illegal = False
        for c in line:
            if c in ["(", "[", "{", "<"]:
                stack.append(c)
                continue

            if c == ")" and stack[-1] == "(":
                del stack[-1]
                continue

            if c == "]" and stack[-1] == "[":
                del stack[-1]
                continue

            if c == "}" and stack[-1] == "{":
                del stack[-1]
                continue

            if c == ">" and stack[-1] == "<":
                del stack[-1]
                continue

            illegal = True
            break

        if illegal:
            corrupted_lines.append(c)
        else:
            stacks.append(stack)

    return stacks, corrupted_lines


def part1() -> int:
    """Part 1."""

    lines = read_file_lines("year_2021/input_10.txt")
    score = 0

    _, corrupted_lines = filter_lines(lines)

    for c in corrupted_lines:

        if c == ")":
            score += 3
        elif c == "]":
            score += 57
        elif c == "}":
            score += 1197
        elif c == ">":
            score += 25137

    return score


def part2() -> int:
    """Part 2."""

    lines = read_file_lines("year_2021/input_10.txt")

    stacks, _ = filter_lines(lines)

    scores = []

    for stack in stacks:
        completion = list(reversed(stack))
        score = 0

        for character in completion:
            score *= 5
            if character == "(":
                score += 1
            elif character == "[":
                score += 2
            elif character == "{":
                score += 3
            elif character == "<":
                score += 4
        scores.append(score)

    scores.sort()
    return scores[int((len(scores) - 1) / 2)]


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
