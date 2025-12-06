"""Day 6"""

from functools import reduce
from itertools import batched
from operator import add, mul, sub, truediv
from aoc.shared import read_file_lines, transpose

_OPERATORS = {"+": add, "-": sub, "*": mul, "/": truediv}

lines = [line.replace("\n", "") for line in read_file_lines("year_2025/input_06.txt", strip=False)]
operations = [_OPERATORS[o] for o in lines[-1].split(" ") if o]


def get_columns() -> list[list[list[str]]]:

    operator_indices = [i for i, c in enumerate(lines[-1]) if c != " "]
    final_operator_width = len(lines[-1]) + 1
    widths = [j - i - 1 for i, j in zip(operator_indices, operator_indices[1:] + [final_operator_width])]

    start_index = 0

    columns = []

    for width in widths:
        column = []
        for line in lines[:-1]:
            cell = line[start_index : start_index + width]
            column.append(list(cell))

        columns.append(column)

        start_index += width + 1  # +1 for the space

    return columns


def part1() -> int:
    """Part 1."""

    total = 0
    for index, row in enumerate(get_columns()):
        operator = operations[index]
        joined_row = ["".join(cell).strip() for cell in row]
        int_row = [int(value) for value in joined_row]
        total += reduce(operator, int_row)

    return total


def part2() -> int:
    """Part 2."""

    total = 0
    for index, row in enumerate(get_columns()):
        int_row = [int("".join(x).strip()) for x in zip(*row)]
        operator = operations[index]
        total += reduce(operator, int_row)

    return total


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
