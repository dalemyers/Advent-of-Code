from typing import Any, Dict, List

from PIL import Image

def chunk(input_list: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into chunks of the specified size."""
    chunks = []
    for i in range(0, len(input_list), chunk_size):
        chunks.append(input_list[i : i + chunk_size])
    return chunks


def render_bw_grid(grid: List[List[int]]) -> str:

    height = len(grid)
    width = len(grid[0])

    img = Image.new('L', (width, height), "black")
    pixels = img.load()

    for y, row in enumerate(grid):
        for x, pixel in enumerate(row):
            pixels[x,y] = pixel

    img.show()



def dict_grid_to_real(grid: Dict[str, Any], default: Any) -> List[List[Any]]:
    min_x = None
    max_x = None
    min_y = None
    max_y = None
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
            try:
                value = grid[key]
            except KeyError:
                value = default
            row.append(value)
        output.append(row)

    return output