from collections import defaultdict

contents = list(map(int, "1,20,8,12,0,14".split(",")))


def play(stop_turn):
    last_seen = {}
    for index, value in enumerate(contents):
        last_seen[value] = [index + 1]
        last_spoken = value

    for turn in range(len(contents) + 1, stop_turn + 1):
        last = last_seen.get(last_spoken, [0, 0])
        count = len(last)
        if count == 1:
            value = 0
        else:
            value = last[-1] - last[-2]

        last_spoken = value
        last_seen[value] = (last_seen.get(value, []) + [turn])[-2:]

    return last_spoken



def part1():
    return play(2020)


def part2():
    return play(30_000_000)


print("Part 1:", part1())
print("Part 2:", part2())
