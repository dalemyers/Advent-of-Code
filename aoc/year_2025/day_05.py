"""Day 5"""

from aoc.shared import read_file

lines = read_file("year_2025/input_05.txt")
ranges_collection, ingredients_collection = lines.split("\n\n")
ranges = [list(map(int, line.split("-"))) for line in ranges_collection.split("\n") if line]
ingredient_ids = [int(line) for line in ingredients_collection.split("\n") if line]


def part1() -> int:
    """Part 1."""

    available = 0

    for ingredient_id in ingredient_ids:
        for ingredient_range in ranges:
            if ingredient_range[0] <= ingredient_id <= ingredient_range[1]:
                available += 1
                break
    return available


def part2() -> int:
    """Part 2."""

    ranges.sort()

    seen_ranges = [ranges[0]]

    for start, end in ranges[1:]:
        for seen in seen_ranges:
            changes = False

            if seen[0] <= start <= seen[1]:
                seen[1] = max(seen[1], end)
                changes = True

            if seen[0] <= end <= seen[1]:
                seen[0] = min(seen[0], start)
                changes = True

            if changes:
                break
        else:
            seen_ranges.append([start, end])

    total = 0
    for start, end in seen_ranges:
        total += (end - start) + 1

    return total


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
