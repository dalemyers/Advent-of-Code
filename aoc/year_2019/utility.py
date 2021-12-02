import time
from typing import Any, Dict, List, Optional, Tuple

from PIL import Image

def chunk(input_list: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into chunks of the specified size."""
    chunks = []
    for i in range(0, len(input_list), chunk_size):
        chunks.append(input_list[i : i + chunk_size])
    return chunks


def position_key(x: int, y: int) -> str:
    return f"{x}/{y}"

def position_from_key(key: str) -> Tuple[int, int]:
    return tuple(map(int, key.split("/")))


def scale_grid(grid: List[List[Any]], scale: int) -> List[List[Any]]:
    output = []
    for row in grid:
        new_row = []
        for pixel in row:
            new_row.extend([pixel] * scale)
        for _ in range(scale):
            output.append(new_row)
    return output


def render_bw_grid(grid: List[List[int]]) -> str:

    height = len(grid)
    width = len(grid[0])

    img = Image.new('L', (width, height), "black")
    pixels = img.load()

    for y, row in enumerate(grid):
        for x, pixel in enumerate(row):
            pixels[x,y] = pixel

    img.show()


def render_grid(grid: List[List[Any]], color_map: Dict[Any, Tuple[int,int,int]]) -> str:

    height = len(grid)
    width = len(grid[0])

    img = Image.new('RGB', (width, height), "white")
    pixels = img.load()

    for y, row in enumerate(grid):
        for x, pixel in enumerate(row):
            pixels[x,y] = color_map[pixel]

    img.show()


def render_ascii(grid: List[List[Any]], ascii_map: Optional[Dict[Any, str]] = None) -> str:

    output = ""

    for row in grid:
        for pixel in row:
            if ascii_map:
                output += ascii_map[pixel]
            else:
                output += pixel
        output += "\n"

    return output


def dict_grid_to_real(grid: Dict[str, Any], default: Any, minimal_bounding: Optional[Tuple[Tuple[int, int], Tuple[int, int]]] = None) -> List[List[Any]]:
    if minimal_bounding is None:
        min_x = None
        max_x = None
        min_y = None
        max_y = None
    else:
        min_x = minimal_bounding[0][0]
        max_x = minimal_bounding[0][1]
        min_y = minimal_bounding[1][0]
        max_y = minimal_bounding[1][1]

    for key in grid.keys():
        x,y = key.split("/")
        x = int(x)
        y = int(y)
        if min_x == None or x < min_x:
            min_x = x
        if max_x == None or x > max_x:
            max_x = x
        if min_y == None or y < min_y:
            min_y = y
        if max_y == None or y > max_y:
            max_y = y

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    output = []

    for y in range(min_y, max_y + 1):
        row = []
        for x in range(min_x, max_x + 1):
            key = f"{x}/{y}"
            if key in grid:
                value = grid[key]
            else:
                value = default
            row.append(value)
        output.append(row)

    return output


class Stopwatch(object):

    name: str
    start: Optional[time.time]
    emd: Optional[time.time]

    def __init__(self, name: str) -> None:
        self.name = name
        self.start = None
        self.end = None

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, type, value, traceback):
        self.end = time.time()

        print(f"{self.name}: {self.end - self.start}")