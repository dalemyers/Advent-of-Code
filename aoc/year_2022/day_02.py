"""Day 2"""

import enum
from typing import List, Tuple
from aoc.shared import read_file_lines

lines = read_file_lines("year_2022/input_02.txt")


class Move(enum.Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

    def score(self) -> int:
        if self == Move.ROCK:
            return 1
        if self == Move.PAPER:
            return 2
        if self == Move.SCISSORS:
            return 3
        raise Exception()

    def beats(self) -> "Move":
        if self == Move.ROCK:
            return Move.SCISSORS
        if self == Move.PAPER:
            return Move.ROCK
        if self == Move.SCISSORS:
            return Move.PAPER
        raise Exception()

    def loses(self) -> "Move":
        if self == Move.ROCK:
            return Move.PAPER
        if self == Move.PAPER:
            return Move.SCISSORS
        if self == Move.SCISSORS:
            return Move.ROCK
        raise Exception()


class Condition(enum.Enum):
    WIN = "Z"
    LOSE = "X"
    DRAW = "Y"


def get_plays1() -> Tuple[Move, Move]:
    output = []
    for line in lines:
        opp, you = line.split(" ")
        if you == "X":
            you = "A"
        elif you == "Y":
            you = "B"
        elif you == "Z":
            you = "C"
        output.append((Move(opp), Move(you)))

    return output


def get_plays2() -> Tuple[Move, Condition]:
    output = []
    for line in lines:
        opp, you = line.split(" ")
        output.append((Move(opp), Condition(you)))

    return output


def part1() -> int:
    """Part 1."""

    rounds = get_plays1()
    total_score = 0
    for them, us in rounds:
        total_score += us.score()

        if us.beats() == them:
            total_score += 6
        elif them.beats() != us:
            total_score += 3

    return total_score


def part2() -> int:
    """Part 2."""

    rounds = get_plays2()
    total_score = 0
    for them, condition in rounds:
        if condition == Condition.WIN:
            total_score += 6
            us = them.loses()
        elif condition == Condition.DRAW:
            total_score += 3
            us = them
        elif condition == Condition.LOSE:
            us = them.beats()

        total_score += us.score()

    return total_score


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
