import enum
import math


with open("year_2016/input_02.txt") as f:
    contents = f.readlines()



def part1():

    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    code = []

    x = 1
    y = 1

    for line in contents:
        line = line.strip()

        for character in line:
            delta_x = 0
            delta_y = 0
            if character == "U":
                delta_y = -1
            elif character == "D":
                delta_y = 1
            elif character == "L":
                delta_x = -1
            else:
                delta_x = 1

            if delta_x == -1 and x != 0:
                x -= 1
            elif delta_x == 1 and x != 2:
                x += 1

            if delta_y == -1 and y != 0:
                y -= 1
            elif delta_y == 1 and y != 2:
                y += 1

        code.append(keypad[y][x])

    return code

def part2():
    keypad = [
        [None, None, 1, None, None],
        [None, 2, 3, 4, None],
        [5, 6, 7, 8, 9],
        [None, 'A', 'B', 'C', None],
        [None, None, 'D', None, None],
    ]

    code = []

    x = 1
    y = 2

    for line in contents:
        line = line.strip()

        for character in line:
            delta_x = 0
            delta_y = 0
            if character == "U":
                delta_y = -1
            elif character == "D":
                delta_y = 1
            elif character == "L":
                delta_x = -1
            else:
                delta_x = 1

            new_x = x
            new_y = y

            if delta_x == -1 and x != 0:
                new_x = x - 1
            elif delta_x == 1 and x != 4:
                new_x = x + 1

            if delta_y == -1 and y != 0:
                new_y = y - 1
            elif delta_y == 1 and y != 4:
                new_y = y + 1

            if keypad[new_y][new_x] is None:
                continue

            x = new_x
            y = new_y

        code.append(keypad[y][x])

    return code


print("Part 1:", part1())
print("Part 2:", part2())
