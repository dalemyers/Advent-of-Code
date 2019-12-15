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

def run_program(noun: int, verb: int) -> int:
    with open("2019/02/input.txt") as f:
        full_input = f.read().strip()

    program = Program(full_input)
    program.set_value(noun, 1)
    program.set_value(verb, 2)

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

    return program.get_value(0)

found_noun = None
found_verb = None

for noun in range(0, 100):
    for verb in range(0, 100):
        result = run_program(noun, verb)
        if result == 19690720:
            found_noun = noun
            found_verb = verb
            break

    if found_noun is not None:
        break

print(100 * found_noun + found_verb)
