from shared import create_bool_grid, create_int_grid

with open("year_2015/input_06.txt") as f:
    contents = f.read()

bool_grid = create_bool_grid(1000, 1000)
int_grid = create_int_grid(1000, 1000)

for index, instruction_string in enumerate(contents.splitlines()):
    print(index)
    components = instruction_string.split(" ")
    if components[0] == "turn":
        components = components[1:]
    action = components[0]
    start = list(map(int, components[1].split(",")))
    end = list(map(int, components[3].split(",")))

    for y in range(start[1], end[1] + 1):
        for x in range(start[0], end[0] + 1):
            if action == "toggle":
                bool_grid[y][x] = not bool_grid[y][x]
                int_grid[y][x] += 2
            elif action == "on":
                bool_grid[y][x] = True
                int_grid[y][x] += 1
            else:
                bool_grid[y][x] = False
                if int_grid[y][x] > 0:
                    int_grid[y][x] -= 1

light_count = 0
brightness_count = 0
for y in range(1000):
    for x in range(1000):
        brightness_count += int_grid[y][x]
        if bool_grid[y][x] == True:
            light_count += 1

print("Part 1:", light_count)
print("Part 2:", brightness_count)
