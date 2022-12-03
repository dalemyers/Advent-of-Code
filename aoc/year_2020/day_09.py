from shared import read_ints_from_file

contents = read_ints_from_file("year_2020/input_09.txt")

LENGTH = 25


def sums(values, target):
    for i in range(len(values)):
        for j in range(len(values)):
            if i == j:
                continue
            if values[i] == values[j]:
                continue
            if values[i] + values[j] == target:
                return True
    return False


def get_non_matching():
    for i in range(LENGTH, len(contents)):
        preceeding = contents[i - LENGTH : i]
        if not sums(preceeding, contents[i]):
            return contents[i]
    return None


def part1():
    return get_non_matching()


def part2():
    target = get_non_matching()
    for i in range(len(contents)):
        for l in range(1, len(contents) - i):
            sequence = contents[i : i + l]
            if sum(sequence) == target:
                return min(sequence) + max(sequence)


print("Part 1:", part1())
print("Part 2:", part2())
