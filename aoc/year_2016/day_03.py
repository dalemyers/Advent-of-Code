import enum
import math


with open("year_2016/input_03.txt") as f:
    contents = f.readlines()

triangles = []
for line in contents:
    line = line.strip()
    components = line.split(" ")
    components = [c.strip() for c in components]
    components = [c for c in components if len(c) > 0]
    triangles.append(list(map(int, components)))


def triangle_is_possible(triangle):
    one = triangle[0] + triangle[1] > triangle[2]
    two = triangle[0] + triangle[2] > triangle[1]
    three = triangle[1] + triangle[2] > triangle[0]
    return one and two and three


def part1():
    possible = 0

    for triangle in triangles:
        if triangle_is_possible(triangle):
            possible += 1

    return possible


def part2():
    possible = 0

    for index in range(0, len(triangles), 3):
        row_1 = triangles[index]
        row_2 = triangles[index + 1]
        row_3 = triangles[index + 2]

        t1 = [row_1[0], row_2[0], row_3[0]]
        t2 = [row_1[1], row_2[1], row_3[1]]
        t3 = [row_1[2], row_2[2], row_3[2]]

        for triangle in [t1, t2, t3]:
            if triangle_is_possible(triangle):
                possible += 1

    return possible

print("Part 1:", part1())
print("Part 2:", part2())
