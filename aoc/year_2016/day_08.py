import enum
from shared import read_file_lines, create_bool_grid, render_bw_grid

contents = read_file_lines("year_2016/input_08.txt")


class Section(enum.Enum):
    row = 1
    column = 2


class Direction(enum.Enum):
    x = 1
    y = 2


def rotate(grid, section, index, magnitude):
    if section == Section.row:
        grid[index] = grid[index][-magnitude:] + grid[index][:-magnitude]
        return

    buffer = []
    for i in range(len(grid)):
        buffer.append(grid[i][index])

    buffer = buffer[-magnitude:] + buffer[:-magnitude]

    for i in range(len(grid)):
        grid[i][index] = buffer[i]


def part1():
    grid = create_bool_grid(50, 6)

    for row in contents:
        if row.startswith("rect "):
            row = row[5:]
            dimensions = list(map(int, row.split("x")))
            for y in range(dimensions[1]):
                for x in range(dimensions[0]):
                    grid[y][x] = True
            continue

        # rotate
        row = row[7:]
        if row.startswith("row"):
            section = Section.row
            row = row[4:]
        else:
            section = Section.column
            row = row[7:]

        # Drop 'x=' or 'y='
        row = row[2:]

        components = list(map(int, row.split(" by ")))
        index = components[0]
        magnitude = components[1]

        rotate(grid, section, index, magnitude)

    render_bw_grid(grid)

    counter = 0
    for row in grid:
        counter += sum([1 if c else 0 for c in row])

    return counter


def part2():
    raise Exception("Interactive from part 1")


print("Part 1:", part1())
print("Part 2:", part2())
