from collections import defaultdict
import copy
from shared import read_file_lines, create_bool_grid_from_contents, print_grid_3d_dict, print_grid_3d

contents = read_file_lines("year_2020/input_17.txt")
input_grid = create_bool_grid_from_contents(contents)

CYCLES = 6


def get_surrounding(grid, z, y, x):
    surrounding = 0
    for z_index in range(z - 1, z + 2):
        if z_index < 0 or z_index >= len(grid):
            continue
        for y_index in range(y - 1, y + 2):
            if y_index < 0 or y_index >= len(grid[z_index]):
                continue
            for x_index in range(x - 1, x + 2):
                if x_index < 0 or x_index >= len(grid[z_index][y_index]):
                    continue
                if z == z_index and y == y_index and x == x_index:
                    continue
                if grid[z_index][y_index][x_index] == "#":
                    surrounding += 1
    return surrounding


def get_surrounding_4d(grid, c, z, y, x):
    surrounding = 0
    for c_index in range(c - 1, c + 2):
        if c_index < 0 or c_index >= len(grid):
            continue
        for z_index in range(z - 1, z + 2):
            if z_index < 0 or z_index >= len(grid[c_index]):
                continue
            for y_index in range(y - 1, y + 2):
                if y_index < 0 or y_index >= len(grid[c_index][z_index]):
                    continue
                for x_index in range(x - 1, x + 2):
                    if x_index < 0 or x_index >= len(grid[c_index][z_index][y_index]):
                        continue
                    if c == c_index and z == z_index and y == y_index and x == x_index:
                        continue
                    if grid[c_index][z_index][y_index][x_index] == "#":
                        surrounding += 1
    return surrounding


def empty_row(length):
    return ["." for _ in range(length)]

def empty_plane(length):
    output = []
    for _ in range(length):
        output.append(empty_row(length))
    return output

def empty_cube(length):
    output = []
    for _ in range(length):
        output.append(empty_plane(length))
    return output


def part1():
    grid = [[[character for character in row] for row in contents]]
    dim = len(contents[0])
    for _ in range(CYCLES):
        dim += 2
        new_grid = copy.deepcopy(grid)
        for pi, plane in enumerate(grid):
            for ri, row in enumerate(plane):
                new_grid[pi][ri] = ["."] + grid[pi][ri] + ["."]
            new_grid[pi] = [empty_row(dim)] + new_grid[pi] + [empty_row(dim)]
        new_grid = [empty_plane(dim)] + new_grid + [empty_plane(dim)]
        grid = new_grid

    for cycle in range(CYCLES):
        buffer = copy.deepcopy(grid)
        for pi, plane in enumerate(grid):
            for ri, row in enumerate(plane):
                for ci, character in enumerate(row):
                    surrounding = get_surrounding(grid, pi, ri, ci)
                    if character == "#":
                        if surrounding not in [2, 3]:
                            buffer[pi][ri][ci] = "."
                    else:
                        if surrounding == 3:
                            buffer[pi][ri][ci] = "#"
        #print_grid_3d(buffer, -CYCLES)
        grid = buffer

    active_count = 0
    for plane in grid:
        for row in plane:
            for character in row:
                if character == "#":
                    active_count += 1

    return active_count




def part2():
    grid = [[[[character for character in row] for row in contents]]]
    dim = len(contents[0])
    for _ in range(CYCLES):
        dim += 2
        new_grid = copy.deepcopy(grid)
        for ci, cube in enumerate(grid):
            for pi, plane in enumerate(cube):
                for ri, row in enumerate(plane):
                    new_grid[ci][pi][ri] = ["."] + grid[ci][pi][ri] + ["."]
                new_grid[ci][pi] = [empty_row(dim)] + new_grid[ci][pi] + [empty_row(dim)]
            new_grid[ci] = [empty_plane(dim)] + new_grid[ci] + [empty_plane(dim)]
        new_grid = [empty_cube(dim)] + new_grid + [empty_cube(dim)]

        grid = new_grid

    for cycle in range(CYCLES):
        buffer = copy.deepcopy(grid)
        for ci, cube in enumerate(grid):
            for pi, plane in enumerate(cube):
                for ri, row in enumerate(plane):
                    for vi, character in enumerate(row):
                        surrounding = get_surrounding_4d(grid, ci, pi, ri, vi)
                        if character == "#":
                            if surrounding not in [2, 3]:
                                buffer[ci][pi][ri][vi] = "."
                        else:
                            if surrounding == 3:
                                buffer[ci][pi][ri][vi] = "#"
        grid = buffer

    active_count = 0
    for cube in grid:
        for plane in cube:
            for row in plane:
                for character in row:
                    if character == "#":
                        active_count += 1

    return active_count


print("Part 1:", part1())
print("Part 2:", part2())
