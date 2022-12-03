with open("year_2015/input_01.txt", encoding="utf-8") as f:
    contents = f.read()


floor = 0
for character in contents:
    if character == "(":
        floor += 1
    elif character == ")":
        floor -= 1

print("Part 1:", floor)

floor = 0
for index, character in enumerate(contents):
    if character == "(":
        floor += 1
    elif character == ")":
        floor -= 1
    if floor == -1:
        print("Part 2:", index + 1)
        break
