input_value = 29_000_000


def part1():
    size = int(input_value / 10)
    house = [0] * size
    for i in range(1, size):
        for j in range(i, size, i):
            house[j] += i * 10

    for index in range(size):
        if house[index] > input_value:
            return index

    return None


def part2():
    size = int(input_value / 11) + 1
    house = [0] * size
    for i in range(1, size):
        deliver_count = 0
        for j in range(i, size, i):
            house[j] += i * 11
            deliver_count += 1
            if deliver_count >= 50:
                break

    for index in range(size):
        if house[index] > input_value:
            return index

    return None


print("Part 1:", part1())
print("Part 2:", part2())
