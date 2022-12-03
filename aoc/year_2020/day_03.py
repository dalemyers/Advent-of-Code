import math


def hash_to_bool(input_lines):
    output = []
    for line in input_lines:
        output_line = []
        line = line.strip()
        for character in line:
            if character == ".":
                output_line.append(False)
            else:
                output_line.append(True)
        output.append(output_line)
    return output


def extend(input_trees, x_delta, y_delta):
    output = []
    slope = x_delta / y_delta
    for line in input_trees:
        factor = math.ceil((len(input_trees) / len(line)) * slope)
        output.append(line * factor)
    return output


with open("year_2020/input_03.txt") as input_file:
    contents = input_file.readlines()

trees = hash_to_bool(contents)


def check_collisions(x_delta, y_delta):
    x = -x_delta
    y = -y_delta
    count = 0

    extended_trees = extend(trees, x_delta, y_delta)

    while True:
        x += x_delta
        y += y_delta
        if y >= len(extended_trees):
            return count
        # if x > len(extended_trees[y]):
        #    x = 0
        if extended_trees[y][x]:
            count += 1


def part1(x_delta=3, y_delta=1):
    return check_collisions(3, 1)


def part2():
    v1 = check_collisions(1, 1)
    v2 = check_collisions(3, 1)
    v3 = check_collisions(5, 1)
    v4 = check_collisions(7, 1)
    v5 = check_collisions(1, 2)
    return v1 * v2 * v3 * v4 * v5


print("Part 1:", part1())
print("Part 2:", part2())
