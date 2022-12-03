from math import factorial

from shared import read_ints_from_file, product

contents = read_ints_from_file("year_2020/input_10.txt")


def part1():
    adapters = sorted(contents)
    adapters = [0] + adapters + [max(adapters) + 3]

    diff_1 = 0
    diff_3 = 0

    for a1, a2 in zip(adapters, adapters[1:]):
        diff = a2 - a1
        if diff == 1:
            diff_1 += 1
        elif diff == 3:
            diff_3 += 1
        else:
            raise Exception()

    return diff_1 * diff_3


def part2():
    adapters = sorted(contents)
    device_adapter = adapters[-1] + 3
    adapters = adapters + [device_adapter]

    paths = {0: 1}

    for adapter in adapters:
        back_1 = paths.get(adapter - 1, 0)
        back_2 = paths.get(adapter - 2, 0)
        back_3 = paths.get(adapter - 3, 0)
        paths[adapter] = back_1 + back_2 + back_3

    return paths[device_adapter]


print("Part 1:", part1())
print("Part 2:", part2())
