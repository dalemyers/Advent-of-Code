import enum
from typing import List, Optional

class Opcode(enum.Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    HALT = 99

class ParameterMode(enum.Enum):
    POSITION = 0
    IMMEDIATE = 1

def run_program(input_list: List[int]) -> int:
    with open("input_05.txt") as f:
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
            Opcode.ADD: 2,
            Opcode.MULTIPLY: 2,
            Opcode.JUMP_IF_TRUE: 2,
            Opcode.JUMP_IF_FALSE: 2,
            Opcode.LESS_THAN: 2,
            Opcode.EQUALS: 2,
        }

        # Make up implied parameters
        parameter_length = parameter_lengths.get(opcode)
        while parameter_length and len(parameter_modes) < parameter_length:
            parameter_modes.append(ParameterMode.POSITION)

        if opcode == Opcode.HALT:
            break

        if opcode == Opcode.JUMP_IF_TRUE:
            value1 = program.get_next(parameter_modes[0])
            value2 = program.get_next(parameter_modes[1])
            if value1 != 0:
                program.index = value2

        if opcode == Opcode.JUMP_IF_FALSE:
            value1 = program.get_next(parameter_modes[0])
            value2 = program.get_next(parameter_modes[1])
            if value1 == 0:
                program.index = value2

        if opcode == Opcode.LESS_THAN:
            value2 = program.get_next(parameter_modes[1])
            output_index = program.get_next()
            if value1 < value2:
                program.set_value(1, output_index)
            else:
                program.set_value(0, output_index)

        if opcode == Opcode.EQUALS:

            value2 = program.get_next(parameter_modes[1])
            output_index = program.get_next()
            if value1 == value2:
                program.set_value(1, output_index)
            else:
                program.set_value(0, output_index)

        if opcode == Opcode.INPUT:

            output_index = program.get_next()
            program.set_value(value, output_index)

        if opcode == Opcode.OUTPUT:
            index1 = program.get_next()
            value1 = program.get_value(index1)
            print(f"OUTPUT: {value1}")

        if opcode == Opcode.ADD:
            value1 = program.get_next(parameter_modes[0])
            value2 = program.get_next(parameter_modes[1])
            output_index = program.get_next()
            output_value = value1 + value2
            program.set_value(output_value, output_index)

        if opcode == Opcode.MULTIPLY:
            value1 = program.get_next(parameter_modes[0])
            value2 = program.get_next(parameter_modes[1])
            output_index = program.get_next()
            output_value = value1 * value2
            program.set_value(output_value, output_index)

    return program.get_value(0)

run_program([1])
run_program([5])