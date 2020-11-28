
with open("year_2015/input_02.txt") as f:
    contents = f.read()


total_area = 0
total_ribbon = 0
for gift in contents.splitlines():
    dimensions = list(map(int, gift.split("x")))

    side1 = dimensions[0] * dimensions[1]
    side2 = dimensions[0] * dimensions[2]
    side3 = dimensions[1] * dimensions[2]
    p1 = (dimensions[0] + dimensions[1]) * 2
    p2 = (dimensions[0] + dimensions[2]) * 2
    p3 = (dimensions[1] + dimensions[2]) * 2
    smallest_side = min(side1, side2, side3)
    smallest_perimeter = min(p1, p2, p3)
    volume = dimensions[0] * dimensions[1] * dimensions[2]
    area = (side1 + side2 + side3) * 2 + smallest_side

    total_area += area
    total_ribbon += smallest_perimeter + volume

print("Part 1:", total_area)
print("Part 2:", total_ribbon)