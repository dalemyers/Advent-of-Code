"""Day 4"""

from collections import defaultdict
from itertools import combinations

from aoc.shared import read_file_lines

lines = read_file_lines("year_2024/input_04.txt")

ABOVE = (-1, 0)
BELOW = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)
UP_RIGHT = (-1, 1)
UP_LEFT = (-1, -1)
DOWN_RIGHT = (1, 1)
DOWN_LEFT = (1, -1)

DIRECTIONS = [ABOVE, BELOW, RIGHT, LEFT, UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT]


def find_letters_in_direction(
    row: int, column: int, dx: int, dy: int, letters: str, original_length: int
) -> tuple[int, int, int, int] | None:
    if letters == "":
        y, x = row, column
        for _ in range(original_length - 1):
            y -= dy
            x -= dx
        return (x, y, dx, dy)

    if row + dy < 0 or row + dy > len(lines) - 1:
        return None

    if column + dx < 0 or column + dx > len(lines[row + dy]) - 1:
        return None

    if lines[row + dy][column + dx] == letters[0]:
        return find_letters_in_direction(row + dy, column + dx, dx, dy, letters[1:], original_length)

    return None


def part1() -> int:
    """Part 1."""

    count = 0

    for row in range(len(lines)):
        for column in range(len(lines[row])):
            character = lines[row][column]
            if character != "X":
                continue

            for dy, dx in DIRECTIONS:
                match = find_letters_in_direction(row - dy, column - dx, dx, dy, "XMAS", len("XMAS"))
                if match:
                    count += 1

    return count


def part2() -> int:
    """Part 2."""

    matches = []
    for row in range(len(lines)):
        for column in range(len(lines[row])):
            character = lines[row][column]
            if character != "M":
                continue

            for dy, dx in DIRECTIONS:
                match = find_letters_in_direction(row - dy, column - dx, dx, dy, "MAS", len("MAS"))
                if match:
                    matches.append(match)

    # They need to have the same center to be a cross.
    matches_by_center = defaultdict(list)

    for x, y, dx, dy in matches:
        center = x + dx, y + dy
        matches_by_center[center].append((x, y, dx, dy))

    # Remove any centers which only have a single match
    keys_to_delete = []

    for center, center_matches in matches_by_center.items():
        if len(center_matches) == 1:
            keys_to_delete.append(center)

    for key in keys_to_delete:
        del matches_by_center[key]

    # Go through each match, and each combination, then remove any which form a
    # plus rather than a cross. Count the remainder.
    count = 0

    for center, center_matches in matches_by_center.items():
        for a, b in combinations(center_matches, 2):
            if 0 in [a[2], a[3], b[2], b[3]]:  # Get rid of "plus" instead of X.
                continue
            count += 1

    return count


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
