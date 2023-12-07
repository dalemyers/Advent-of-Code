"""Day 7"""

from collections import Counter
import enum
from aoc.shared import read_file_lines

lines = read_file_lines("year_2023/input_07.txt")


class HandResult(enum.Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    PAIR = 2
    HIGH_CARD = 1


CARD_VALUES = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

CARD_VALUES_2 = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


def get_result(hand: str) -> HandResult:
    c = Counter(hand)

    if len(c) == 1:
        return HandResult.FIVE_OF_A_KIND

    if len(c) == 2:
        if 4 in c.values():
            return HandResult.FOUR_OF_A_KIND
        return HandResult.FULL_HOUSE

    if len(c) == 3:
        if 3 in c.values():
            return HandResult.THREE_OF_A_KIND
        return HandResult.TWO_PAIR

    if len(c) == 4:
        return HandResult.PAIR

    return HandResult.HIGH_CARD


def part1() -> int:
    """Part 1."""

    results = []
    for line in lines:
        cards, bid_str = line.split(" ")
        result = get_result(cards)
        results.append((result, cards, int(bid_str)))

    results.sort(
        key=lambda r: (
            r[0].value,
            CARD_VALUES[r[1][0]],
            CARD_VALUES[r[1][1]],
            CARD_VALUES[r[1][2]],
            CARD_VALUES[r[1][3]],
            CARD_VALUES[r[1][4]],
        )
    )

    total = 0

    for i, (_, _, bid) in enumerate(results):
        total += (i + 1) * bid

    return total


def part2() -> int:
    """Part 2."""

    results = []
    for line in lines:
        cards, bid_str = line.split(" ")
        c = Counter(cards)
        if "J" in c:
            del c["J"]
        if len(c) == 0:  # All jokers
            replaced_hand = "AAAAA"
        else:
            replaced_hand = cards.replace("J", c.most_common()[0][0])
        result = get_result(replaced_hand)
        results.append((result, cards, int(bid_str)))

    results.sort(
        key=lambda r: (
            r[0].value,
            CARD_VALUES_2[r[1][0]],
            CARD_VALUES_2[r[1][1]],
            CARD_VALUES_2[r[1][2]],
            CARD_VALUES_2[r[1][3]],
            CARD_VALUES_2[r[1][4]],
        )
    )

    total = 0

    for i, (_, _, bid) in enumerate(results):
        total += (i + 1) * bid

    return total


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
