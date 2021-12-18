"""Day 8"""

from typing import Set
from aoc.shared import read_file_lines
from aoc.shared.input import read_file_lines

segment_count_map = {
    0: [],
    1: [],
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8],
}


def part1() -> int:
    """Part 1."""

    raw_notes = read_file_lines("year_2021/input_08.txt")
    notes = []

    for note in raw_notes:
        signal_patterns_string, output_value_string = note.split(" | ")
        signal_patterns = [set(s) for s in signal_patterns_string.split(" ")]
        output_values = [set(s) for s in output_value_string.split(" ")]
        notes.append((signal_patterns, output_values))

    results = {1: 0, 4: 0, 7: 0, 8: 0}

    for _, output_patterns in notes:
        for pattern in output_patterns:
            if len(pattern) == 2:
                results[1] += 1
            elif len(pattern) == 3:
                results[7] += 1
            elif len(pattern) == 4:
                results[4] += 1
            elif len(pattern) == 7:
                results[8] += 1

    return results[1] + results[4] + results[7] + results[8]


def solve(signal_patterns: Set[int], output_patterns: Set[int]) -> int:
    a = None
    b = None
    c = None
    d = None
    e = None
    f = None
    g = None

    results = {}

    for pattern in signal_patterns:
        if len(pattern) == 2:
            results[1] = pattern
        elif len(pattern) == 3:
            results[7] = pattern
        elif len(pattern) == 4:
            results[4] = pattern
        elif len(pattern) == 7:
            results[8] = pattern

    a = results[7] - results[1]

    changes = True
    while changes:
        changes = False

        for pattern in signal_patterns:

            if len(pattern) not in [5, 6]:
                continue

            if len(pattern) == 5:

                if 2 not in results and len(pattern - results[4]) == 3:
                    changes = True
                    results[2] = pattern
                    break

                if 3 not in results and len(pattern - results[1]) == 3:
                    changes = True
                    results[3] = pattern
                    break

                if (
                    5 not in results
                    and len(pattern - results[1]) == 4
                    and len(results[4] - pattern) == 1
                ):
                    changes = True
                    results[5] = pattern
                    break

            if len(pattern) == 6:

                if 9 not in results and len(pattern - results[4]) == 2:
                    changes = True
                    results[9] = pattern
                    break

                if 6 not in results and len(pattern - results[1]) == 5:
                    changes = True
                    results[6] = pattern
                    break

                if (
                    0 not in results
                    and len(pattern - results[4]) == 3
                    and len(pattern - results[7]) == 3
                ):
                    changes = True
                    results[0] = pattern
                    break

        if b is None:
            if 0 in results and 2 in results:
                changes = True
                b = results[0] - results[2] - results[1]
            elif 3 in results:
                changes = True
                b = results[4] - results[3]

        if c is None and 6 in results:
            changes = True
            c = results[8] - results[6]

        if d is None and 0 in results:
            changes = True
            d = results[8] - results[0]

        if e is None and 9 in results:
            changes = True
            e = results[8] - results[9]

        if f is None and c:
            changes = True
            f = results[1] - c

        if g is None and 9 in results and a:
            changes = True
            g = results[9] - results[4] - a

    a = list(a)[0]
    b = list(b)[0]
    c = list(c)[0]
    d = list(d)[0]
    e = list(e)[0]
    f = list(f)[0]
    g = list(g)[0]

    if {a, b, c, d, e, f, g} != {"a", "b", "c", "d", "e", "f", "g"}:
        return 0

    corrections = {
        a: "a",
        b: "b",
        c: "c",
        d: "d",
        e: "e",
        f: "f",
        g: "g",
    }

    output = ""
    for pattern in output_patterns:
        corrected_pattern = {corrections[l] for l in pattern}
        if corrected_pattern == {"a", "b", "c", "e", "f", "g"}:
            output += "0"
        elif corrected_pattern == {"c", "f"}:
            output += "1"
        elif corrected_pattern == {"a", "c", "d", "e", "g"}:
            output += "2"
        elif corrected_pattern == {"a", "c", "d", "f", "g"}:
            output += "3"
        elif corrected_pattern == {"b", "c", "d", "f"}:
            output += "4"
        elif corrected_pattern == {"a", "b", "d", "f", "g"}:
            output += "5"
        elif corrected_pattern == {"a", "b", "d", "e", "f", "g"}:
            output += "6"
        elif corrected_pattern == {"a", "c", "f"}:
            output += "7"
        elif corrected_pattern == {"a", "b", "c", "d", "e", "f", "g"}:
            output += "8"
        elif corrected_pattern == {"a", "b", "c", "d", "f", "g"}:
            output += "9"
        else:
            return -1

    return int(output)


def part2() -> int:
    """Part 2."""

    raw_notes = read_file_lines("year_2021/input_08.txt")
    notes = []

    for note in raw_notes:
        signal_patterns_string, output_value_string = note.split(" | ")
        signal_patterns = [set(s) for s in signal_patterns_string.split(" ")]
        output_values = [set(s) for s in output_value_string.split(" ")]
        notes.append((signal_patterns, output_values))

    total = 0
    for signal_patterns, output_patterns in notes:
        total += solve(signal_patterns, output_patterns)

    return total


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
