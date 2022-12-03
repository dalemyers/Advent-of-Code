from shared import read_ints_from_file

values = read_ints_from_file("year_2020/input_01.txt")


def part1():
    v_set = set(values)
    for value in v_set:
        other = 2020 - value
        if other in v_set:
            return other * value
    return None


def part2():
    v_set = set(values)
    for index1, value1 in enumerate(values):
        for index2, value2 in enumerate(values):
            if index1 == index2:
                continue
            other = 2020 - value1 - value2

            # Check if it is even there
            if other not in v_set:
                continue

            # It was there, so now we need to get the position
            for index3, value3 in enumerate(values):
                if value3 == other and index1 != index3 and index2 != index3:
                    return other * value1 * value2

    return None


print("Part 1:", part1())
print("Part 2:", part2())
