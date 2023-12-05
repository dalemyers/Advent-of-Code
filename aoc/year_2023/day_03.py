"""Day 3"""

from aoc.shared import read_file_lines

lines = read_file_lines("year_2023/input_03.txt")


def find_symbols(input: list[str], symbols: str) -> list[tuple[int, int]]:
    symbol_locations = []
    for y, line in enumerate(input):
        for x, character in enumerate(line):
            if character in symbols:
                symbol_locations.append((x, y))
    return sorted(symbol_locations, key=lambda f: (f[1], f[0]))


def extend_number(lines: list[str], x: int, y: int) -> list[tuple[int, int, int]]:
    digits = [(x, y, lines[y][x])]
    for delta in range(x + 1, len(lines[y])):
        # For the case x is right at the edge
        if delta >= len(lines[y]):
            break

        if lines[y][delta].isdigit():
            digits.append((delta, y, lines[y][delta]))
            continue

        if len(digits) >= 2:
            return digits

        break

    if len(digits) >= 2:
        return digits

    # TODO: What if there's one to the left _AND_ right?

    digits = [(x, y, lines[y][x])]
    for delta in range(x - 1, -1, -1):
        # For the case x is right at the edge
        if x <= 0:
            break

        if lines[y][delta].isdigit():
            digits = [(delta, y, lines[y][delta])] + digits
            continue

        if len(digits) >= 2:
            return digits

        break

    return digits


def find_numbers(
    x_symbol: int,
    y_symbol: int,
) -> list[list[int]]:
    numbers = []
    for y in range(y_symbol - 1, y_symbol + 2):
        if y < 0:
            continue
        if y >= len(lines):
            continue
        for x in range(x_symbol - 1, x_symbol + 2):
            if x < 0:
                continue
            if x >= len(lines[y]):
                continue

            if lines[y][x] == "." or not lines[y][x].isdigit():
                continue

            numbers.append(extend_number(lines, x, y))

    return numbers


def remove_identicals(values: list[list[tuple[int, int, int]]]) -> list[list[tuple[int, int, int]]]:
    output = []
    for line in values:
        if line in output:
            continue
        output.append(line)
    return output


def collapse_ranges(values: list[list[tuple[int, int, int]]]) -> list[list[tuple[int, int, int]]]:
    output = []
    for line_a in values:
        a_start = line_a[0][0]
        a_end = line_a[-1][0]

        keep_a = True
        for line_b in values:
            # If there y component isn't the same, ignore them.
            if line_a[0][1] != line_b[0][1]:
                continue
            if line_a == line_b:
                continue
            b_start = line_b[0][0]
            b_end = line_b[-1][0]

            if a_start <= b_end and b_start <= a_end:
                if len(line_a) < len(line_b):
                    keep_a = False

        if keep_a:
            output.append(line_a)

    return output


def simplify_number(number):
    return int("".join(n[2] for n in number))


def part1() -> int:
    """Part 1."""

    start_symbols = find_symbols(lines, "-@*/&#%+=$")

    symbol_numbers = []
    for x_symbol, y_symbol in start_symbols:
        symbol_numbers += find_numbers(x_symbol, y_symbol)

    symbol_numbers.sort(key=lambda line: line[0][1])
    symbol_numbers = remove_identicals(symbol_numbers)
    symbol_numbers = collapse_ranges(symbol_numbers)
    simplified_numbers = [simplify_number(number) for number in symbol_numbers]

    return sum(simplified_numbers)


def part2() -> int:
    """Part 2."""

    start_symbols = find_symbols(lines, "*")

    total_ratios = 0

    symbol_numbers = []
    for x_symbol, y_symbol in start_symbols:
        symbol_numbers.append((x_symbol, y_symbol, find_numbers(x_symbol, y_symbol)))

    for x_symbol, y_symbol, numbers in symbol_numbers:
        numbers = remove_identicals(numbers)
        numbers = collapse_ranges(numbers)
        if len(numbers) != 2:
            continue
        simplified_numbers = [simplify_number(number) for number in numbers]
        ratio = simplified_numbers[0] * simplified_numbers[1]
        total_ratios += ratio

    return total_ratios


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
