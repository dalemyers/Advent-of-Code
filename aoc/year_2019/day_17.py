import enum
from typing import List, Optional, Tuple

import intcode
import utility


class Turn(enum.Enum):
    RIGHT = "R"
    LEFT = "L"


class Direction(enum.Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"

    def opposite(self) -> "Direction":
        if self == Direction.UP:
            return Direction.DOWN
        if self == Direction.DOWN:
            return Direction.UP
        if self == Direction.LEFT:
            return Direction.RIGHT
        if self == Direction.RIGHT:
            return Direction.LEFT

    def is_opposite(self, direction: "Direction") -> bool:
        return self == direction.opposite()

    def turn_to_commands(self, direction: "Direction") -> Turn:
        if self == direction:
            raise Exception("Already facing direction")

        if self == direction.opposite():
            return Turn.RIGHT

        if self == Direction.UP:
            if direction == Direction.RIGHT:
                return Turn.RIGHT
            elif direction == Direction.LEFT:
                return Turn.LEFT

        if self == Direction.RIGHT:
            if direction == Direction.DOWN:
                return Turn.RIGHT
            elif direction == Direction.UP:
                return Turn.LEFT

        if self == Direction.DOWN:
            if direction == Direction.LEFT:
                return Turn.RIGHT
            elif direction == Direction.RIGHT:
                return Turn.LEFT

        if self == Direction.LEFT:
            if direction == Direction.UP:
                return Turn.RIGHT
            elif direction == Direction.DOWN:
                return Turn.LEFT


class Camera:

    output: List[List[str]]
    current_row: List[str]
    computer: intcode.Computer

    def __init__(
        self, input_values: List[int], enable_robot: bool = False, input_callback=None
    ) -> None:
        self.computer = intcode.Computer(program=input_values)
        self.computer.output_callback = self.render_character
        self.computer.input_callback = input_callback
        self.output = []
        self.current_row = []

        if enable_robot:
            self.computer.set_value(2, 0)

    def get_character(self, x, y) -> Optional[str]:
        try:
            return self.output[y][x]
        except IndexError:
            return None

    def run(self) -> None:
        self.computer.run()

    def render_character(self, name: str, value: int) -> None:
        character = chr(value)
        if character != "\n":
            self.current_row.append(character)
        else:
            self.output.append(self.current_row)
            self.current_row = []


def part1(input_values) -> None:
    camera = Camera(input_values)
    camera.run()

    intersections = []

    for y in range(len(camera.output)):
        for x in range(len(camera.output[y])):
            if camera.output[y][x] == "#":
                try:
                    neighbors = ""
                    neighbors += camera.output[y][x - 1]
                    neighbors += camera.output[y][x + 1]
                    neighbors += camera.output[y - 1][x]
                    neighbors += camera.output[y + 1][x]
                    if neighbors == "####":
                        intersections.append((x, y))
                except:
                    continue

    total = 0
    for x, y in intersections:
        total += x * y
    print("Part 1:", total)


class InputMode(enum.Enum):
    MAIN = 1
    A = 2
    B = 3
    C = 4


class Pathfinder:

    camera: Camera
    x: int
    y: int
    droid_direction: Optional[Direction]

    def __init__(self, input_values: List[int]) -> None:
        self.camera = Camera(input_values, True, self.get_input)
        self.x = 0
        self.y = 0
        self.droid_direction = None
        self.input_mode = InputMode.MAIN
        self.total_dust = 0

    def run(self) -> None:
        self.camera.run()

    def dust_collector(self, name: str, value: int) -> None:
        self.total_dust = value

    def get_input(self, name: str) -> int:
        if self.droid_direction is None:
            self.find_droid()
            self.find_route()
            self.camera.computer.output_callback = self.dust_collector

        if self.input_mode == InputMode.MAIN:
            if len(self.full_output) > 0:
                return ord(self.full_output.pop(0))
            else:
                self.input_mode = InputMode.A
                return ord("\n")

        if self.input_mode == InputMode.A:
            if len(self.a) > 0:
                return ord(self.a.pop(0))
            else:
                self.input_mode = InputMode.B
                return ord("\n")

        if self.input_mode == InputMode.B:
            if len(self.b) > 0:
                return ord(self.b.pop(0))
            else:
                self.input_mode = InputMode.C
                return ord("\n")

        if self.input_mode == InputMode.C:
            if len(self.c) > 0:
                return ord(self.c.pop(0))
            else:
                return ord("\n")

        return 0

    def determine_next_direction(
        self, previous_direction: Optional[Direction] = None
    ) -> Optional[Direction]:
        if (
            previous_direction != Direction.LEFT
            and self.camera.get_character(self.x + 1, self.y) == "#"
        ):
            return Direction.RIGHT

        if (
            previous_direction != Direction.RIGHT
            and self.camera.get_character(self.x - 1, self.y) == "#"
        ):
            return Direction.LEFT

        if (
            previous_direction != Direction.UP
            and self.camera.get_character(self.x, self.y + 1) == "#"
        ):
            return Direction.DOWN

        if (
            previous_direction != Direction.DOWN
            and self.camera.get_character(self.x, self.y - 1) == "#"
        ):
            return Direction.UP

        return None

    def move_forward_as_far_as_possible(self) -> int:
        forward_count = 0
        while True:
            if (
                self.droid_direction == Direction.UP
                and self.camera.get_character(self.x, self.y - 1) == "#"
            ):
                forward_count += 1
                self.y = self.y - 1
            elif (
                self.droid_direction == Direction.DOWN
                and self.camera.get_character(self.x, self.y + 1) == "#"
            ):
                forward_count += 1
                self.y = self.y + 1
            elif (
                self.droid_direction == Direction.RIGHT
                and self.camera.get_character(self.x + 1, self.y) == "#"
            ):
                forward_count += 1
                self.x = self.x + 1
            elif (
                self.droid_direction == Direction.LEFT
                and self.camera.get_character(self.x - 1, self.y) == "#"
            ):
                forward_count += 1
                self.x = self.x - 1
            else:
                break
        return forward_count

    def compress(self, full_output: List):
        def all_slices(array):
            for length in range(2, min(21, len(array) + 1), 2):
                for start_index in range(0, len(array) - length + 1):
                    if array[start_index] not in ["L", "R"]:
                        continue
                    yield start_index, array[start_index : start_index + length]

        def occurences(subarray, array) -> List[int]:
            if len(subarray) > len(array):
                return []
            start_index = 0
            indices = []
            while True:
                if len(array) - start_index < len(subarray):
                    break

                found = True
                for a, b in zip(subarray, array[start_index:]):
                    if a != b:
                        found = False
                        break
                if found:
                    indices.append(start_index)
                start_index += 1
            return indices

        def combine(array):
            return ",".join(map(str, array))

        def validate_slice(array_slice: List) -> bool:
            if "A" in array_slice or "B" in array_slice or "C" in array_slice:
                return False

            if len(array_slice) < 6:
                return False

            if len(combine(array_slice)) > 20:
                return False

            return True

        viable = None

        for _, array_slice_a in all_slices(full_output):
            if viable:
                break

            if not validate_slice(array_slice_a):
                continue

            indices_a = occurences(array_slice_a, full_output)

            compressed_a = full_output[:]
            for index in reversed(indices_a):
                compressed_a = (
                    compressed_a[:index] + ["A"] + compressed_a[index + len(array_slice_a) :]
                )

            for _, array_slice_b in all_slices(compressed_a):
                if viable:
                    break

                if not validate_slice(array_slice_b):
                    continue

                indices_b = occurences(array_slice_b, compressed_a)

                compressed_b = compressed_a[:]
                for index in reversed(indices_b):
                    compressed_b = (
                        compressed_b[:index] + ["B"] + compressed_b[index + len(array_slice_b) :]
                    )

                for _, array_slice_c in all_slices(compressed_b):
                    if viable:
                        break

                    if not validate_slice(array_slice_c):
                        continue

                    indices_c = occurences(array_slice_c, compressed_b)

                    compressed_c = compressed_b[:]
                    for index in reversed(indices_c):
                        compressed_c = (
                            compressed_c[:index]
                            + ["C"]
                            + compressed_c[index + len(array_slice_c) :]
                        )

                    if len(combine(compressed_c)) > 20:
                        continue

                    non_sub = False
                    for value in compressed_c:
                        if value not in ["A", "B", "C"]:
                            non_sub = True
                            break

                    if non_sub:
                        continue

                    viable = (array_slice_a, array_slice_b, array_slice_c, compressed_c)

        self.a = list(combine(viable[0]))
        self.b = list(combine(viable[1]))
        self.c = list(combine(viable[2]))
        self.full_output = list(combine(viable[3]))

    def find_route(self) -> None:

        full_output = []

        # Try and navigate to the end
        while True:

            # Turn to the next direction
            required_direction = self.determine_next_direction(self.droid_direction)

            if required_direction is None:
                break

            full_output.append(self.droid_direction.turn_to_commands(required_direction).value)
            self.droid_direction = required_direction

            # Try and move forward as far as possible
            forward_count = self.move_forward_as_far_as_possible()
            full_output.append(forward_count)

        self.compress(full_output)

    def find_droid(self):
        for y in range(len(self.camera.output)):
            if self.droid_direction is not None:
                break

            for x in range(len(self.camera.output[y])):
                if self.droid_direction is not None:
                    break

                if self.camera.output[y][x] in "^v<>":
                    self.x, self.y = x, y
                    self.droid_direction = Direction(self.camera.output[y][x])


def part2(input_values) -> None:
    pathfinder = Pathfinder(input_values)
    pathfinder.run()
    print("Part 2:", pathfinder.total_dust)


with open("year_2019/input_17.txt") as input_file:
    contents = input_file.read()

input_values = list(map(int, contents.split(",")))

part1(input_values)
part2(input_values)
