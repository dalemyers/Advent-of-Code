with open("year_2015/input_03.txt") as f:
    contents = f.read()


x = 0
y = 0
grid = {}


grid[x] = {}
grid[x][y] = 1

for direction in contents:
    if direction == "^":
        y += 1
    elif direction == "v":
        y -= 1
    elif direction == ">":
        x += 1
    elif direction == "<":
        x -= 1
    if grid.get(x) is None:
        grid[x] = {}
    if grid[x].get(y) is None:
        grid[x][y] = 0
    grid[x][y] += 1

total = 0
for x_index, column in grid.items():
    for y_index, count in column.items():
        if count > 0:
            total += 1

print("Part 1:", total)


positions = {True: [0, 0], False: [0, 0]}

grid = {}
grid[0] = {}
grid[0][0] = 1


user = True

for direction in contents:
    user = not user
    if direction == "^":
        positions[user][1] += 1
    elif direction == "v":
        positions[user][1] -= 1
    elif direction == ">":
        positions[user][0] += 1
    elif direction == "<":
        positions[user][0] -= 1
    x = positions[user][0]
    y = positions[user][1]
    if grid.get(x) is None:
        grid[x] = {}
    if grid[x].get(y) is None:
        grid[x][y] = 0
    grid[x][y] += 1

total = 0
for x_index, column in grid.items():
    for y_index, count in column.items():
        if count > 0:
            total += 1

print("Part 2:", total)
