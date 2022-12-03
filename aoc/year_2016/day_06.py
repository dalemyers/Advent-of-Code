import collections


with open("year_2016/input_06.txt", encoding="utf-8") as f:
    contents = f.readlines()
contents = [c.strip() for c in contents]


def part1():

    counters = []
    for _ in range(len(contents[0])):
        counters.append(collections.Counter())

    for line in contents:
        for index, character in enumerate(line):
            counters[index].update(character)

    output = ""
    for counter in counters:
        most_common = None
        for key in set(counter.elements()):
            count = counter[key]
            if most_common is None or count > counter[most_common]:
                most_common = key

        output += most_common

    return output


def part2():

    counters = []
    for _ in range(len(contents[0])):
        counters.append(collections.Counter())

    for line in contents:
        for index, character in enumerate(line):
            counters[index].update(character)

    output = ""
    for counter in counters:
        least_common = None
        for key in set(counter.elements()):
            count = counter[key]
            if least_common is None or count < counter[least_common]:
                least_common = key

        output += least_common

    return output


print("Part 1:", part1())
print("Part 2:", part2())
