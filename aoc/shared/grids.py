from typing import Any, List, Optional, Tuple

from PIL import Image


def create_int_grid(width: int, height: int, default: int = 0):
    return [[default for x in range(width)] for y in range(height)]


def create_bool_grid(width: int, height: int, default: bool = False):
    return [[default for x in range(width)] for y in range(height)]


def create_bool_grid_from_contents(contents: List[List[str]], *, true_char: str = "#"):
    return [[character == true_char for character in row] for row in contents]


def render_bw_grid(grid: List[List[bool]]) -> None:

    height = len(grid)
    width = len(grid[0])

    img = Image.new("L", (width, height), "black")
    pixels = img.load()

    for y, row in enumerate(grid):
        for x, pixel in enumerate(row):
            pixels[x, y] = 255 if pixel else 0

    img.show()


def print_raw_grid(grid):
    for row in grid:
        print("".join(row))
    print()


def print_full_empty_grid(grid):
    for row in grid:
        text = ["#" if v else "." for v in row]
        print("".join(text))
    print()


def print_small_int_grid(grid):
    for row in grid:
        print("".join([str(v) for v in row]))
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


def get_surrounding_points(
    y: int,
    x: int,
    grid: List[List[Any]],
    *,
    diagonals: bool = False,
    height: Optional[int] = None,
    width: Optional[int] = None,
) -> List[Tuple[int, int]]:
    points = []

    if height is None:
        height = len(grid)

    if width is None:
        width = len(grid[0])

    if y - 1 >= 0:
        points.append((y - 1, x))
    if y + 1 < height:
        points.append((y + 1, x))
    if x - 1 >= 0:
        points.append((y, x - 1))
    if x + 1 < width:
        points.append((y, x + 1))

    if not diagonals:
        return points

    if y - 1 >= 0 and x - 1 >= 0:
        points.append((y - 1, x - 1))
    if y + 1 < height and x + 1 < width:
        points.append((y + 1, x + 1))
    if y - 1 >= 0 and x + 1 < width:
        points.append((y - 1, x + 1))
    if y + 1 < height and x - 1 >= 0:
        points.append((y + 1, x - 1))

    return points
