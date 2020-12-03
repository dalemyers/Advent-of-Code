from itertools import combinations
from functools import reduce
from shared import create_int_grid


ROW = 3010
COLUMN = 3019
MAX_INDEX = max(ROW, COLUMN)


def part1():
    grid = create_int_grid(MAX_INDEX*2 + 1, MAX_INDEX*2 + 1)
    x = 1
    y = 1

    x_max = 1
    y_max = 1

    value = 20151125
    while True:
        if y == 0 or x > x_max:
            y_max += 1
            x_max += 1
            y = y_max
            x = 1
            continue
        if y > MAX_INDEX*2 or x > MAX_INDEX*2:
            break
        grid[y][x] = value
        value = (value * 252_533) % 33_554_393
        x += 1
        y -= 1

    return grid[ROW][COLUMN]

def part2():
    return None


print("Part 1:", part1())
print("Part 2:", part2())