import enum
from typing import Dict, List

import intcode
import utility

class Tile(enum.Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


class Screen:

    grid: Dict[str, Tile]
    input_buffer: List[int]

    def __init__(self):
        self.grid = {}
        self.input_buffer = []

    def receive_input(self, value) -> None:
        self.input_buffer.append(value)

        if len(self.input_buffer) != 3:
            return

        x, y, tile_id = self.input_buffer
        self.input_buffer = []

        tile = Tile(tile_id)

        key = utility.position_key(x, y)
        self.grid[key] = tile

    def count_of(self, tile: Tile) -> int:
        count = 0
        for key, value in self.grid.items():
            if value == tile:
                count += 1
        return count


with open("year_2019/input_13.txt") as input_file:
    contents = input_file.read()

input_values = list(map(int, contents.split(",")))

screen = Screen()

computer = intcode.Computer(program=input_values)
computer.output_callback = lambda name, value: screen.receive_input(value)
computer.run()

print(screen.count_of(Tile.BLOCK))
