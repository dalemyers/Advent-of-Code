from itertools import combinations
from functools import reduce
from shared import read_ints_from_file


def group(number_of_groups):
    values = read_ints_from_file("year_2015/input_24.txt")
    values = sorted(values)

    smallest_product = reduce(lambda x, y: x * y, values)
    expected_weight = int(sum(values) / number_of_groups)

    solutions = []

    for n in range(1, len(values) // number_of_groups):
        solution = [x for x in combinations(values, n) if sum(x) == expected_weight]
        solutions.extend(solution)

    solutions = sorted(solutions, key=lambda x: len(x))

    smallest_len = min([len(x) for x in solutions])

    smallest_combinations = [c for c in solutions if len(c) == smallest_len]

    for c in smallest_combinations:
        p = reduce(lambda x, y: x * y, c)
        smallest_product = min(smallest_product, p)

    return smallest_product


def part1():
    return group(3)


def part2():
    return group(4)


print("Part 1:", part1())
print("Part 2:", part2())
