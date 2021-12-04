import os
from typing import Any, Iterable, List

from PIL import Image


def read_file_lines(path):
    base_path = os.path.dirname(__file__)
    aoc_path = os.path.abspath(os.path.join(base_path, ".."))
    with open(os.path.join(aoc_path, path), encoding="utf-8") as input_file:
        contents = input_file.readlines()
    return [c.strip() for c in contents]


def create_int_grid(width: int, height: int, default: int = 0):
    return [[default for x in range(width)] for y in range(height)]


def create_bool_grid(width: int, height: int, default: bool = False):
    return [[default for x in range(width)] for y in range(height)]


def create_bool_grid_from_contents(contents: List[List[str]], *, true_char: str = "#"):
    return [[character == true_char for character in row] for row in contents]


def is_int(value) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


def read_ints_from_file(path: str) -> List[int]:
    base_path = os.path.dirname(__file__)
    aoc_path = os.path.abspath(os.path.join(base_path, ".."))
    with open(os.path.join(aoc_path, path), encoding="utf-8") as f:
        input_data = f.readlines()
    return list(map(int, input_data))


def get_positions(input_list: List[Any], value: Any) -> List[int]:
    positions = []
    for index, input_value in enumerate(input_list):
        if input_value == value:
            positions.append(index)
    return positions


def find_locations(input_list: List[Any], value: List[Any]) -> List[int]:
    locations = []
    for start_index in range(0, len(input_list) - len(value) + 1):
        input_range = input_list[start_index : start_index + len(value)]
        if value == input_range:
            locations.append(start_index)
    return locations


def render_bw_grid(grid: List[List[bool]]) -> None:

    height = len(grid)
    width = len(grid[0])

    img = Image.new("L", (width, height), "black")
    pixels = img.load()

    for y, row in enumerate(grid):
        for x, pixel in enumerate(row):
            pixels[x, y] = 255 if pixel else 0

    img.show()


def product(iterable: Iterable) -> Any:
    value = 1
    for i in iterable:
        value = value * i
    return value


def print_raw_grid(grid):
    for row in grid:
        print("".join(row))
    print()


def print_grid(grid):
    for row in grid:
        text = ["#" if v else "." for v in row]
        print("".join(text))
    print()


def print_grid_3d_dict(grid):
    plane_indices = sorted(list(grid.keys()))
    for plane_index in plane_indices:
        plane = grid[plane_index]
        print(f"z={plane_index}")

        row_indices = sorted(list(plane.keys()))
        for row_index in row_indices:
            row = plane[row_index]

            column_indices = sorted(list(row.keys()))
            row_values = [row[i] for i in column_indices]
            print("".join(row_values))
        print()
    print()


def print_grid_3d(grid, z_start):
    z = z_start
    for plane in grid:
        print(f"z={z}")
        z += 1
        for row in plane:
            print("".join(row))
        print()
    print()


def transpose(values: List[List[Any]]) -> List[List[Any]]:
    return list(map(list, zip(*values)))
