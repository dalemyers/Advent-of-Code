import enum
from typing import Dict, List

import intcode

class Color(enum.Enum):
    BLACK = 0
    WHITE = 1

class Orientation(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def turn_left(self) -> 'Orientation':
        if self == Orientation.NORTH:
            return Orientation.WEST
        if self == Orientation.EAST:
            return Orientation.NORTH
        if self == Orientation.SOUTH:
            return Orientation.EAST
        if self == Orientation.WEST:
            return Orientation.SOUTH

    def turn_right(self) -> 'Orientation':
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

    def next_mode(self) -> 'OutputMode':
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

    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.grid = {}
        self.painted_count = 0
        self.output_mode = OutputMode.COLOR
        self.orientation = Orientation.NORTH

    def position_key(self) -> str:
        return f"{self.x}/{self.y}"

    def get_current_color(self) -> Color:
        key = self.position_key()
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
        min_x = None
        max_x = None
        min_y = None
        max_y = None
        for key in self.grid.keys():
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
        output = ""
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                key = f"{x}/{y}"
                try:
                    color = self.grid[key]
                except KeyError:
                    color = Color.BLACK
                if color == Color.BLACK:
                    output += '#'
                else:
                    output += ' '
            output += "\n"
        return output



with open("year_2019/input_11.txt") as input_file:
    contents = input_file.read()

input_values = list(map(int, contents.split(",")))

def part1():
    robot = Robot()
    computer = intcode.Computer(program=input_values)
    computer.output_callback = lambda name, value: robot.handle_output(value)
    computer.input_callback = lambda name: robot.get_current_color().value
    computer.run()
    print(robot.render_grid())
    print(robot.painted_count)


part1()
