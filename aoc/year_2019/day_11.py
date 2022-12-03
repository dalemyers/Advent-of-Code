import enum
from typing import Dict, List

from PIL import Image

import intcode
import utility


class Color(enum.Enum):
    BLACK = 0
    WHITE = 1


class Orientation(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def turn_left(self) -> "Orientation":
        if self == Orientation.NORTH:
            return Orientation.WEST
        if self == Orientation.EAST:
            return Orientation.NORTH
        if self == Orientation.SOUTH:
            return Orientation.EAST
        if self == Orientation.WEST:
            return Orientation.SOUTH

    def turn_right(self) -> "Orientation":
        if self == Orientation.NORTH:
            return Orientation.EAST
        if self == Orientation.EAST:
            return Orientation.SOUTH
        if self == Orientation.SOUTH:
            return Orientation.WEST
        if self == Orientation.WEST:
            return Orientation.NORTH


class OutputMode(enum.Enum):
    COLOR = 1
    DIRECTION = 2

    def next_mode(self) -> "OutputMode":
        if self == OutputMode.COLOR:
            return OutputMode.DIRECTION

        if self == OutputMode.DIRECTION:
            return OutputMode.COLOR


class Robot:

    x: int
    y: int
    grid: Dict[str, Color]
    painted_count: int
    output_mode: OutputMode
    orientation: Orientation
    flip_initial_panel: bool

    def __init__(self, flip_initial_panel=False) -> None:
        self.x = 0
        self.y = 0
        self.flip_initial_panel = flip_initial_panel
        self.grid = {}
        self.painted_count = 0
        self.output_mode = OutputMode.COLOR
        self.orientation = Orientation.NORTH

    def position_key(self) -> str:
        return f"{self.x}/{self.y}"

    def get_current_color(self) -> Color:
        key = self.position_key()
        if self.flip_initial_panel:
            self.flip_initial_panel = False
            return Color.WHITE
        return self.grid.get(key, Color.BLACK)

    def handle_output(self, value) -> None:
        if self.output_mode == OutputMode.COLOR:
            color = Color(value)
            key = self.position_key()
            current_color = self.grid.get(key, None)
            if current_color == None:
                self.painted_count += 1
            self.grid[key] = color

        elif self.output_mode == OutputMode.DIRECTION:
            if value == 0:
                self.orientation = self.orientation.turn_left()
            else:
                self.orientation = self.orientation.turn_right()

            if self.orientation == Orientation.NORTH:
                self.y -= 1
            elif self.orientation == Orientation.SOUTH:
                self.y += 1
            elif self.orientation == Orientation.EAST:
                self.x += 1
            elif self.orientation == Orientation.WEST:
                self.x -= 1

        self.output_mode = self.output_mode.next_mode()

    def render_grid(self) -> str:
        color_corrected = {k: 0 if v == Color.BLACK else 255 for k, v in self.grid.items()}
        corrected_grid = utility.dict_grid_to_real(color_corrected, 1)
        utility.render_bw_grid(corrected_grid)


with open("year_2019/input_11.txt") as input_file:
    contents = input_file.read()

input_values = list(map(int, contents.split(",")))


def run(flip_initial_panel):
    robot = Robot(flip_initial_panel)
    computer = intcode.Computer(program=input_values)
    computer.output_callback = lambda name, value: robot.handle_output(value)
    computer.input_callback = lambda name: robot.get_current_color().value
    computer.run()
    return robot


def part1():
    print(run(False).painted_count)


def part2():
    run(True).render_grid()


part1()
part2()
