import enum
from typing import Callable, Dict, List, Tuple

import intcode
import utility

class Tile(enum.Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4

TILE_COLOR_MAP = {
    Tile.EMPTY: (255, 255, 255),
    Tile.WALL: (142, 100, 0),
    Tile.BLOCK: (0, 0, 0),
    Tile.PADDLE: (0, 0, 255),
    Tile.BALL: (255, 0, 0),
}

TILE_ASCII_MAP = {
    Tile.EMPTY: ' ',
    Tile.WALL:  '@',
    Tile.BLOCK: '#',
    Tile.PADDLE: '-',
    Tile.BALL: 'O',
}


class Screen:

    grid: Dict[str, Tile]
    input_buffer: List[int]
    score: int
    ball_position: Tuple[int, int]
    paddle_position: Tuple[int, int]

    def __init__(self):
        self.grid = {}
        self.input_buffer = []
        self.score = 0

    def receive_input(self, value) -> None:
        self.input_buffer.append(value)

        if len(self.input_buffer) != 3:
            return

        x, y, tile_id = self.input_buffer
        self.input_buffer = []

        if x == -1 and y == 0:
            self.score = tile_id
            return

        tile = Tile(tile_id)

        if tile == Tile.PADDLE:
            self.paddle_position = (x, y)

        if tile == Tile.BALL:
            self.ball_position = (x, y)

        key = utility.position_key(x, y)
        self.grid[key] = tile

    def render(self):
        real = utility.dict_grid_to_real(self.grid, Tile.EMPTY)
        utility.render_grid(real, TILE_COLOR_MAP)

    def render_ascii(self) -> str:
        real = utility.dict_grid_to_real(self.grid, Tile.EMPTY)
        return utility.render_ascii(real, TILE_ASCII_MAP) + "\n" + str(self.score) + "\n"

    def count_of(self, tile: Tile) -> int:
        count = 0
        for key, value in self.grid.items():
            if value == tile:
                count += 1
        return count

class Joystick:

    ball_position_callback: Callable
    paddle_position_callback: Callable

    def __init__(self, ball_position_callback: Callable, paddle_position_callback: Callable) -> None:
        self.ball_position_callback = ball_position_callback
        self.paddle_position_callback = paddle_position_callback

    def get_direction(self) -> int:
        bx, by = self.ball_position_callback()
        px, py = self.paddle_position_callback()

        if bx < px:
            return -1
        elif bx == px:
            return 0
        elif bx > px:
            return 1


def part1(input_values) -> None:
    screen = Screen()

    computer = intcode.Computer(program=input_values)
    computer.output_callback = lambda name, value: screen.receive_input(value)
    computer.run()

    print(screen.count_of(Tile.BLOCK))


with open("year_2019/input_13.txt") as input_file:
    contents = input_file.read()

input_values = list(map(int, contents.split(",")))

#part1(input_values)


screen = Screen()

def get_ball_position() -> Tuple[int, int]:
    return screen.ball_position

def get_paddle_position() -> Tuple[int, int]:
    #print(screen.render_ascii())
    print(screen.score)
    return screen.paddle_position

joystick = Joystick(get_ball_position, get_paddle_position)


computer = intcode.Computer(program=input_values)
computer.set_value(2, 0)
computer.output_callback = lambda name, value: screen.receive_input(value)
computer.input_callback = lambda name: joystick.get_direction()
computer.run()


print(screen.render_ascii())
