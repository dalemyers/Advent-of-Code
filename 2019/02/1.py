import enum
from typing import List

class Opcode(enum.Enum):
    ADD = 1
    MULTIPLY = 2
    HALT = 99

class Program:

    integers: List[int]
    index: int

    def __init__(self, integers: str) -> None:
        self.integers = list(map(int, integers.split(",")))
        self.index = 0

    def get_next(self) -> int:
        value = self.integers[self.index]
        self.index += 1
        return value

    def get_value(self, index: int) -> int:
        return self.integers[index]

    def set_value(self, value: int, index: int) -> None:
        self.integers[index] = value

    def state(self) -> str:
        return ",".join(map(str, self.integers))


with open("2019/02/input.txt") as f:
    full_input = f.read().strip()

program = Program(full_input)
program.set_value(12, 1)
program.set_value(2, 2)

while True:
    opcode = Opcode(program.get_next())

    if opcode == Opcode.HALT:
        break

    index1 = program.get_next()
    index2 = program.get_next()
    output_index = program.get_next()

    value1 = program.get_value(index1)
    value2 = program.get_value(index2)

    if opcode == Opcode.ADD:
        output_value = value1 + value2

    if opcode == Opcode.MULTIPLY:
        output_value = value1 * value2

    program.set_value(output_value, output_index)

print(program.get_value(0))
