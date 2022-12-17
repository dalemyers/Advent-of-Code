"""Day 13"""

import ast
import functools
from typing import List, Tuple
from aoc.shared import read_chunked

raw_chunks = read_chunked("year_2022/input_13.txt")

DEBUG = False


def debug_print(string: str) -> None:
    if DEBUG:
        print(string)


def load_packet_pairs() -> List[Tuple[List, List]]:
    output = []
    for chunk in raw_chunks:
        new_chunk = []
        for l in chunk.split("\n"):
            new_chunk.append(ast.literal_eval(l))
        output.append(tuple(new_chunk))

    return output


def load_all_packets() -> List[List]:
    output = []
    pairs = load_packet_pairs()
    for p1, p2 in pairs:
        output.append(p1)
        output.append(p2)
    return output


def print_result(result: bool, indent: int) -> None:
    if result:
        debug_print(
            "  " * (indent + 1)
            + "- Left side is smaller, so inputs are in the right order"
        )
    else:
        debug_print(
            "  " * (indent + 1)
            + "- Right side is smaller, so inputs are not in the right order"
        )


def compare_int_list(left: List[int], right: List[int], indent: int) -> int:

    for l, r in zip(left, right):
        debug_print("  " * indent + f"- Compare {l} vs {r}")

        if l == r:
            continue

        print_result(l < r, indent)

        return -1 if l < r else 1

    if len(left) > len(right):
        debug_print(
            "  " * indent
            + "- Right side ran out of items, so inputs are not in the right order"
        )
        return 1

    if len(left) < len(right):
        debug_print(
            "  " * indent
            + "- Left side ran out of items, so inputs are in the right order"
        )
        return -1

    return 0


def compare(left, right, indent: int = 0) -> int:
    debug_print("  " * indent + f"- Compare {left} vs {right}")

    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0

        print_result(left < right, indent)
        return -1 if left < right else 1

    if isinstance(left, list) and isinstance(right, list):
        left_all_ints = all(isinstance(x, int) for x in left)
        right_all_ints = all(isinstance(x, int) for x in right)

        if left_all_ints and right_all_ints:
            return compare_int_list(left, right, indent + 1)

        for l, r in zip(left, right):
            result = compare(l, r, indent + 1)
            if result == 0:
                continue
            return result

        if len(left) > len(right):
            debug_print(
                "  " * (indent + 1)
                + "- Right side ran out of items, so inputs are not in the right order"
            )
            return 1

        if len(left) < len(right):
            debug_print(
                "  " * (indent + 1)
                + "- Left side ran out of items, so inputs are in the right order"
            )
            return -1

        return 0

    if isinstance(left, int) and isinstance(right, list):
        debug_print(
            "  " * indent
            + f"- Mixed types; convert left to [{left}] and retry comparison"
        )
        return compare([left], right, indent)

    if isinstance(left, list) and isinstance(right, int):
        debug_print(
            "  " * indent
            + f"- Mixed types; convert right to [{right}] and retry comparison"
        )
        return compare(left, [right], indent)

    raise Exception("Should never reach here")


def part1() -> int:
    """Part 1."""
    packets = load_packet_pairs()
    in_order = []

    for index, pair in enumerate(packets):
        debug_print(f"== Pair {index + 1} ==")
        if compare(*pair, 0) == -1:
            in_order.append(index + 1)

    return sum(in_order)


def part2() -> int:
    """Part 2."""
    div1 = [[2]]
    div2 = [[6]]

    packets = load_all_packets()
    packets.append(div1)
    packets.append(div2)

    packets.sort(key=functools.cmp_to_key(compare))

    result = 1
    for index, packet in enumerate(packets):
        if packet == div1:
            result *= index + 1
        elif packet == div2:
            result *= index + 1

    return result


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
