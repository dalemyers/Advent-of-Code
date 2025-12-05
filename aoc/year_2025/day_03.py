"""Day 3"""

from aoc.shared import read_file_lines

lines = read_file_lines("year_2025/input_03.txt")


def part1() -> int:
    """Part 1."""

    total = 0
    for bank in lines:
        max_val = 0
        for a_index in range(0, len(bank)):
            for b_index in range(a_index + 1, len(bank)):
                value = int(bank[a_index]) * 10 + int(bank[b_index])
                if value > max_val:
                    max_val = value
        total += max_val
    return total


def max_number(digits: str, k: int) -> str:
    to_remove = len(digits) - k
    stack = []

    for digit in digits:
        # While we have removals left and current digit is larger than stack top,
        # remove the smaller digit from the stack
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    # If we still have removals left, remove from the end
    # (these are already in decreasing order)
    while to_remove > 0:
        stack.pop()
        to_remove -= 1

    return "".join(stack)


def part2() -> int:
    """Part 2."""

    total = 0
    for bank in lines:
        total += int(max_number(bank, 12))

    return total


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
