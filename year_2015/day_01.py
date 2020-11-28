
with open("year_2015/input_01.txt") as f:
    contents = f.read()


floor = 0
for character in contents:
    if character == "(":
        floor += 1
    elif character == ")":
        floor -= 1

print("Part 1:", floor)

