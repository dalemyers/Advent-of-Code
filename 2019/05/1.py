import enum
from typing import List, Optional

class Opcode(enum.Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    HALT = 99

class ParameterMode(enum.Enum):
    POSITION = 0
    IMMEDIATE = 1

class Program:

    integers: List[int]
    index: int

    def __init__(self, integers: str) -> None:
        self.integers = list(map(int, integers.split(",")))
        self.index = 0

    def get_next(self, parameter_mode: Optional[ParameterMode] = None) -> int:
        value = self.integers[self.index]
        self.index += 1

        if not parameter_mode or parameter_mode == ParameterMode.IMMEDIATE:
            return value
        else:
            return self.integers[value]

    def get_value(self, index: int) -> int:
        return self.integers[index]

    def set_value(self, value: int, index: int) -> None:
        self.integers[index] = value

    def state(self) -> str:
        return ",".join(map(str, self.integers))

def run_program(input_list: List[int]) -> int:
    with open("2019/05/input.txt") as f:
        full_input = f.read().strip()

    program = Program(full_input)

    while True:
        instruction_value = program.get_next()
        opcode_value = instruction_value % 100
        opcode = Opcode(opcode_value)
        instruction_value -= opcode_value
        instruction_value //= 100

        parameter_modes = []

        while instruction_value > 0:
            mode_value = instruction_value % 10
            instruction_value -= mode_value
            instruction_value //= 10
            parameter_modes.append(ParameterMode(mode_value))

        parameter_lengths = {
            Opcode.ADD: 3,
            Opcode.MULTIPLY: 3,
            Opcode.OUTPUT: 1
        }

        # Make up implied parameters
        parameter_length = parameter_lengths.get(opcode)
        while parameter_length and len(parameter_modes) < parameter_length:
            parameter_modes.append(ParameterMode.POSITION)

        if opcode == Opcode.HALT:
            break

        if opcode == Opcode.INPUT:
            value = input_list.pop(0)
            output_index = program.get_next()
            program.set_value(value, output_index)

        if opcode == Opcode.OUTPUT:
            index1 = program.get_next(parameter_modes[0])
            print(f"OUTPUT: {index1}")

        if opcode in [Opcode.ADD, Opcode.MULTIPLY]:
            value1 = program.get_next(parameter_modes[0])
            value2 = program.get_next(parameter_modes[1])
            output_index = program.get_next()

            if opcode == Opcode.ADD:
                output_value = value1 + value2

            if opcode == Opcode.MULTIPLY:
                output_value = value1 * value2

            program.set_value(output_value, output_index)

    return program.get_value(0)

run_program([1])