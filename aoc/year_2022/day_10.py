"""Day 10"""

from typing import List
from aoc.shared import read_file_lines


lines = read_file_lines("year_2022/input_10.txt")


class Instruction:

    name: str
    duration: int

    def __init__(self, name: str, duration: int) -> None:
        self.name = name
        self.duration = duration


class Addx(Instruction):

    value: int

    def __init__(self, value: int) -> None:
        super().__init__("addx", 2)
        self.value = value


class Noop(Instruction):
    def __init__(self) -> None:
        super().__init__("noop", 1)


class CPU:

    x: int
    clock: int
    instruction_queue: List[Instruction]
    values: List[int]

    def __init__(self) -> None:
        self.x = 1
        self.clock = 0
        self.instruction_queue = []
        self.values = []

    def cycle(self) -> None:
        self.values.append(self.x)
        instruction = self.instruction_queue.pop(0)
        if isinstance(instruction, Addx):
            self.x += instruction.value
        self.clock += 1

    def run(self, instructions: List[Instruction]) -> None:
        for instruction in instructions:
            if instruction.duration == 1:
                self.instruction_queue.append(instruction)
            else:
                self.instruction_queue += [Noop()] * (instruction.duration - 1)
                self.instruction_queue.append(instruction)

        while len(self.instruction_queue) > 0:
            self.cycle()


def load_instructions() -> List[Instruction]:
    instructions = []
    for line in lines:
        if " " in line:
            name, value = line.split(" ")
        else:
            name = line
            value = None

        if name == "noop":
            instructions.append(Noop())
        elif name == "addx":
            instructions.append(Addx(int(value)))

    return instructions


def part1() -> int:
    """Part 1."""

    instructions = load_instructions()

    cpu = CPU()
    cpu.run(instructions)

    strength = 0
    for i in range(20, len(cpu.values), 40):
        strength += cpu.values[i - 1] * i

    return strength


def part2() -> str:
    """Part 2."""
    instructions = load_instructions()

    cpu = CPU()
    cpu.run(instructions)

    crt_rows = []

    for y in range(0, int(len(cpu.values) / 40)):
        crt_row = []
        for x in range(0, 40):
            cycle = y * 40 + x
            sprite_center = cpu.values[cycle]
            sprite_pixels = (sprite_center - 1, sprite_center, sprite_center + 1)
            sprite_row = ["." if c not in sprite_pixels else "#" for c in range(40)]
            crt_row.append(sprite_row[x])

        crt_rows.append(crt_row)

    output = "\n"
    for row in crt_rows:
        output += "".join(row) + "\n"

    return output


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
