import enum
from typing import Callable, List, Optional

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

def input_list_wrapper(input_list: List[int]):
    def wrapper() -> int:
        return input_list.pop(0)
    return wrapper

class Program:

    integers: List[int]
    index: int
    input_callback: Optional[Callable]
    output_callback: Optional[Callable]

    def __init__(self, integers: List[int], input_callback: Optional[Callable] = None, output_callback: Optional[Callable] = None) -> None:
        self.integers = integers
        self.index = 0
        self.input_callback = input_callback
        self.output_callback = output_callback

    @staticmethod
    def from_string(string_integers: str) -> 'Program':
        return Program(list(map(int, string_integers.split(","))))

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

    def run(self) -> Optional[int]:

        while True:
            instruction_value = self.get_next()
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
                value1 = self.get_next(parameter_modes[0])
                value2 = self.get_next(parameter_modes[1])
                if value1 != 0:
                    self.index = value2

            if opcode == Opcode.JUMP_IF_FALSE:
                value1 = self.get_next(parameter_modes[0])
                value2 = self.get_next(parameter_modes[1])
                if value1 == 0:
                    self.index = value2

            if opcode == Opcode.LESS_THAN:
                value2 = self.get_next(parameter_modes[1])
                output_index = self.get_next()
                if value1 < value2:
                    self.set_value(1, output_index)
                else:
                    self.set_value(0, output_index)

            if opcode == Opcode.EQUALS:

                value2 = self.get_next(parameter_modes[1])
                output_index = self.get_next()
                if value1 == value2:
                    self.set_value(1, output_index)
                else:
                    self.set_value(0, output_index)

            if opcode == Opcode.INPUT:
                assert self.input_callback is not None
                value = self.input_callback()
                output_index = self.get_next()
                self.set_value(value, output_index)

            if opcode == Opcode.OUTPUT:
                index1 = self.get_next()
                value1 = self.get_value(index1)
                if self.output_callback:
                    self.output_callback(value1)
                else:
                    print(f"OUTPUT: {value1}")

            if opcode == Opcode.ADD:
                value1 = self.get_next(parameter_modes[0])
                value2 = self.get_next(parameter_modes[1])
                output_index = self.get_next()
                output_value = value1 + value2
                self.set_value(output_value, output_index)

            if opcode == Opcode.MULTIPLY:
                value1 = self.get_next(parameter_modes[0])
                value2 = self.get_next(parameter_modes[1])
                output_index = self.get_next()
                output_value = value1 * value2
                self.set_value(output_value, output_index)

        return self.get_value(0)
