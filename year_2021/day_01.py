from shared import read_ints_from_file

values = read_ints_from_file("year_2021/input_01.txt")

def part1():
    increasing = 0
    for current, previous in zip(values[1:], values[:-1]):
        if current > previous:
            increasing += 1
    return increasing

def part2():
    increasing = 0

    windows = []

    for i in range(len(values) - 2):
        windows.append(values[i: i + 3])

    for current, previous in zip(windows[1:], windows[:-1]):
        if sum(current) > sum(previous):
            increasing += 1

    return increasing


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
