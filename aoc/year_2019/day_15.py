import enum
import random
from typing import Callable, Dict, List, Optional, Tuple

import astar

import intcode
import pathfinding
import utility

class Movement(enum.Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

class DroidStatus(enum.Enum):
    HIT_WALL = 0
    MOVED_STEP = 1
    MOVED_STEP_AT_OXYGEN = 2

class Tile(enum.Enum):
    DROID = "D"
    WALL = "#"
    TRAVERSABLE = " "
    UNEXPLORED = "."
    OXYGEN = "O"

class RepairDroid:

    grid: Dict[str, Tile]
    last_move: Optional[Movement]
    x: int
    y: int
    computer: intcode.Computer
    next_direction: Optional[Movement]

    direction_map = {
        "N": Movement.NORTH,
        "E": Movement.EAST,
        "S": Movement.SOUTH,
        "W": Movement.WEST,
    }

    def __init__(self, input_values: List[int]) -> None:
        self.step_count = 0
        self.grid = {}
        self.last_move = None
        self.x = 0
        self.y = 0
        self.computer = intcode.Computer(program=input_values)
        self.computer.input_callback = self.get_input
        self.computer.output_callback = self.droid_move
        self.next_direction = Movement.NORTH
        self.grid[utility.position_key(self.x, self.y)] = Tile.DROID

    def run(self) -> None:
        self.computer.run()

    def get_input(self, name: str) -> int:
        self.step_count += 1

        if self.step_count > 5000:
            self.computer.halt()

        self.last_move = self.next_direction
        return self.next_direction.value

    def calculate_next_direction(self, status: DroidStatus) -> None:

        anti_clockwise_movement = {
            Movement.NORTH: Movement.WEST,
            Movement.EAST: Movement.NORTH,
            Movement.SOUTH: Movement.EAST,
            Movement.WEST: Movement.SOUTH,
        }

        clockwise_movement = {
            Movement.NORTH: Movement.EAST,
            Movement.EAST: Movement.SOUTH,
            Movement.SOUTH: Movement.WEST,
            Movement.WEST: Movement.NORTH,
        }

        if status == DroidStatus.HIT_WALL:
            self.next_direction = anti_clockwise_movement[self.last_move]
        else:
            self.next_direction = clockwise_movement[self.last_move]

    def droid_move(self, name: str, value: int) -> None:
        status = DroidStatus(value)

        self.calculate_next_direction(status)

        if status == DroidStatus.HIT_WALL:
            if self.last_move == Movement.NORTH:
                self.grid[utility.position_key(self.x, self.y - 1)] = Tile.WALL
            elif self.last_move == Movement.EAST:
                self.grid[utility.position_key(self.x + 1, self.y)] = Tile.WALL
            elif self.last_move == Movement.SOUTH:
                self.grid[utility.position_key(self.x, self.y + 1)] = Tile.WALL
            elif self.last_move == Movement.WEST:
                self.grid[utility.position_key(self.x - 1, self.y)] = Tile.WALL

            return

        if self.grid.get(utility.position_key(self.x, self.y), Tile.UNEXPLORED) != Tile.OXYGEN:
            self.grid[utility.position_key(self.x, self.y)] = Tile.TRAVERSABLE

        if status == DroidStatus.MOVED_STEP_AT_OXYGEN:
            if self.last_move == Movement.NORTH:
                self.grid[utility.position_key(self.x, self.y - 1)] = Tile.OXYGEN
            elif self.last_move == Movement.EAST:
                self.grid[utility.position_key(self.x + 1, self.y)] = Tile.OXYGEN
            elif self.last_move == Movement.SOUTH:
                self.grid[utility.position_key(self.x, self.y + 1)] = Tile.OXYGEN
            elif self.last_move == Movement.WEST:
                self.grid[utility.position_key(self.x - 1, self.y)] = Tile.OXYGEN

        if self.last_move == Movement.NORTH:
            self.y -= 1
        elif self.last_move == Movement.EAST:
            self.x += 1
        elif self.last_move == Movement.SOUTH:
            self.y += 1
        elif self.last_move == Movement.WEST:
            self.x -= 1

        if self.grid.get(utility.position_key(self.x, self.y), Tile.UNEXPLORED) != Tile.OXYGEN:
            self.grid[utility.position_key(self.x, self.y)] = Tile.DROID

    def render(self, force: bool = False):
        if not force and self.step_count % 1000 != 0:
            return
        grid_list = utility.dict_grid_to_real(self.grid, Tile.UNEXPLORED, ((-10, 10), (-10, 10)))
        print(utility.render_ascii(grid_list, {value: value.value for value in Tile}))
        if not force:
            print(self.step_count)


def get_open_neighbors(node, droid):
    output = []
    x, y = node

    if droid.grid.get(utility.position_key(x-1, y)) in [Tile.TRAVERSABLE, Tile.OXYGEN, Tile.DROID]:
        output.append((x-1, y))
    if droid.grid.get(utility.position_key(x+1, y)) in [Tile.TRAVERSABLE, Tile.OXYGEN, Tile.DROID]:
        output.append((x+1, y))
    if droid.grid.get(utility.position_key(x, y-1)) in [Tile.TRAVERSABLE, Tile.OXYGEN, Tile.DROID]:
        output.append((x, y-1))
    if droid.grid.get(utility.position_key(x, y+1)) in [Tile.TRAVERSABLE, Tile.OXYGEN, Tile.DROID]:
        output.append((x, y+1))

    return output


def part1(input_values) -> None:
    droid = RepairDroid(input_values)
    droid.run()

    droid.grid[utility.position_key(0, 0)] = Tile.DROID
    droid.render(force=True)

    start = (0, 0)

    for key, value in droid.grid.items():
        if value != Tile.OXYGEN:
            continue
        end = utility.position_from_key(key)
        break

    def distance_between(n1, n2):
        return pathfinding.distance(n1[0], n1[1], n2[0], n2[1])

    results = astar.find_path(
        start,
        end,
        lambda node: get_open_neighbors(node, droid),
        distance_between_fnct=distance_between,
        heuristic_cost_estimate_fnct=distance_between
    )

    result_path = list(results)

    for x, y in result_path:
        droid.grid[utility.position_key(x, y)] = Tile.DROID

    droid.render(force=True)

    print("Part 1:", len(result_path) - 1)


def part2(input_values) -> None:
    droid = RepairDroid(input_values)
    droid.run()

    for key, value in droid.grid.items():
        if value != Tile.OXYGEN:
            continue
        oxygen = utility.position_from_key(key)
        break

    assert oxygen is not None

    iteration_count = 0
    next_iteration = [oxygen]
    while len(next_iteration) > 0:
        iteration_count += 1
        buffer = []
        for cell in next_iteration:
            neighbors = get_open_neighbors(cell, droid)
            for neighbor in neighbors:
                if droid.grid.get(utility.position_key(neighbor[0], neighbor[1]), Tile.UNEXPLORED) in [Tile.TRAVERSABLE, Tile.DROID]:
                    buffer.append(neighbor)
        for cell in next_iteration:
            droid.grid[utility.position_key(cell[0], cell[1])] = Tile.OXYGEN
        next_iteration = buffer

    print("Part 2:", iteration_count - 1)


with open("year_2019/input_15.txt") as input_file:
    contents = input_file.read()

input_values = list(map(int, contents.split(",")))

part1(input_values)
part2(input_values)