import enum
from typing import Callable, List, Optional, Tuple

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
    def wrapper(name) -> int:
        return input_list.pop(0)
    return wrapper

class HaltException(Exception):
    pass

class Computer:

    name: int
    is_halted: bool
    program: List[int]
    index: int
    input_callback: Optional[Callable]
    output_callback: Optional[Callable]

    def __init__(self, *, name: str = "", program: List[int], input_callback: Optional[Callable] = None, output_callback: Optional[Callable] = None) -> None:
        self.name = name
        self.is_halted = False
        self.program = program[:]
        self.index = 0
        self.input_callback = input_callback
        self.output_callback = output_callback

    @staticmethod
    def from_string(string_integers: str) -> 'Program':
        return Program(list(map(int, string_integers.split(","))))

    def get_next(self, parameter_mode: Optional[ParameterMode] = None) -> int:
        value = self.peek_next(parameter_mode=parameter_mode)
        self.index += 1
        return value

    def peek_next(self, parameter_mode: Optional[ParameterMode] = None) -> int:
        value = self.program[self.index]

        if not parameter_mode or parameter_mode == ParameterMode.IMMEDIATE:
            return value
        else:
            return self.program[value]

    def peek_next_instruction(self) -> Opcode:
        value = self.program[self.index]
        opcode, _ = Computer.opcode_parameters(value)
        return opcode

    def get_value(self, index: int) -> int:
        return self.program[index]

    def set_value(self, value: int, index: int) -> None:
        self.program[index] = value

    def state(self) -> str:
        return ",".join(map(str, self.program))

    @staticmethod
    def opcode_parameters(instruction_value) -> Tuple[Opcode, List[ParameterMode]]:
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

        return opcode, parameter_modes


    def do_next(self) -> Opcode:
        if self.is_halted:
            return Opcode.HALT

        instruction_value = self.get_next()
        opcode, parameter_modes = Computer.opcode_parameters(instruction_value)

        if opcode == Opcode.HALT:
            self.is_halted = True
            raise HaltException()

        if opcode == Opcode.JUMP_IF_TRUE:
            value1 = self.get_next(parameter_modes[0])
            value2 = self.get_next(parameter_modes[1])
            if value1 != 0:
                self.index = value2
            return opcode

        if opcode == Opcode.JUMP_IF_FALSE:
            value1 = self.get_next(parameter_modes[0])
            value2 = self.get_next(parameter_modes[1])
            if value1 == 0:
                self.index = value2
            return opcode

        if opcode == Opcode.LESS_THAN:
            value1 = self.get_next(parameter_modes[0])
            value2 = self.get_next(parameter_modes[1])
            output_index = self.get_next()
            if value1 < value2:
                self.set_value(1, output_index)
            else:
                self.set_value(0, output_index)
            return opcode

        if opcode == Opcode.EQUALS:
            value1 = self.get_next(parameter_modes[0])
            value2 = self.get_next(parameter_modes[1])
            output_index = self.get_next()
            if value1 == value2:
                self.set_value(1, output_index)
            else:
                self.set_value(0, output_index)
            return opcode

        if opcode == Opcode.INPUT:
            assert self.input_callback is not None
            value = self.input_callback(self.name)
            output_index = self.get_next()
            self.set_value(value, output_index)
            return opcode

        if opcode == Opcode.OUTPUT:
            index1 = self.get_next()
            value1 = self.get_value(index1)
            if self.output_callback:
                self.output_callback(self.name, value1)
            else:
                print(f"OUTPUT: {value1}")
            return opcode

        if opcode == Opcode.ADD:
            value1 = self.get_next(parameter_modes[0])
            value2 = self.get_next(parameter_modes[1])
            output_index = self.get_next()
            output_value = value1 + value2
            self.set_value(output_value, output_index)
            return opcode

        if opcode == Opcode.MULTIPLY:
            value1 = self.get_next(parameter_modes[0])
            value2 = self.get_next(parameter_modes[1])
            output_index = self.get_next()
            output_value = value1 * value2
            self.set_value(output_value, output_index)
            return opcode

        assert False, "Never should reach here"

        return opcode

    def try_do_next(self) -> Opcode:
        try:
            return self.do_next()
        except HaltException:
            return Opcode.HALT

    def run(self) -> None:

        while True:
            try:
                self.do_next()
            except HaltException:
                break
