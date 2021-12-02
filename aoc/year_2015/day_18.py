import copy
from shared import create_bool_grid, create_int_grid

with open("year_2015/input_18.txt") as f:
    contents = f.readlines()


def print_grid(grid):
    for row in grid:
        text = ["#" if v else "." for v in row]
        print("".join(text))
    print()

SIZE = len(contents[0].strip())

def run(stick_corners=False):
    bool_grid = create_bool_grid(SIZE, SIZE)

    for y, instruction_string in enumerate(contents):
        for x, character in enumerate(instruction_string.strip()):
            bool_grid[y][x] = True if character == "#" else False

    print_grid(bool_grid)

    for i in range(100):
        buffer = copy.deepcopy(bool_grid)
        for y in range(SIZE):
            for x in range(SIZE):
                if stick_corners:
                    if (y == 0 and x == 0) or (y == SIZE - 1 and x == 0) or (y == 0 and x == SIZE - 1) or (y == SIZE - 1 and x == SIZE - 1):
                        buffer[y][x] = True
                        continue
                upper_left = bool_grid[y-1][x-1] if y >= 1 and x >= 1 else False
                upper = bool_grid[y-1][x] if y >= 1 else False
                upper_right = bool_grid[y-1][x+1] if y >= 1 and x < SIZE - 1 else False
                left = bool_grid[y][x-1] if x >= 1 else False
                right = bool_grid[y][x+1] if x < SIZE - 1 else False
                lower_left = bool_grid[y+1][x-1] if y < SIZE - 1 and x >= 1 else False
                lower = bool_grid[y+1][x] if y < SIZE - 1 else False
                lower_right = bool_grid[y+1][x+1] if y < SIZE - 1 and x < SIZE - 1 else False
                on = sum([upper_left, upper, upper_right, right, lower_right, lower, lower_left, left])
                if bool_grid[y][x]:
                    buffer[y][x] = on in [2,3]
                else:
                    buffer[y][x] = on == 3

        bool_grid = buffer

        #print_grid(bool_grid)

    total = 0
    for y in range(SIZE):
        total += sum(bool_grid[y])
    return total

print("Part 1:", run(False))
print("Part 2:", run(True))