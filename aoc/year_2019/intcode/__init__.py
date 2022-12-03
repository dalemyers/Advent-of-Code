import enum
from typing import Callable, Dict, List, Optional, Tuple


class Opcode(enum.Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    RELATIVE_BASE_OFFSET = 9
    HALT = 99


class ParameterMode(enum.Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


def input_list_wrapper(input_list: List[int]):
    def wrapper(name) -> int:
        return input_list.pop(0)

    return wrapper


class HaltException(Exception):
    pass


class Computer:

    name: int
    is_halted: bool
    program: Dict[int, int]
    index: int
    relative_base: int
    input_callback: Optional[Callable]
    output_callback: Optional[Callable]

    def __init__(
        self,
        *,
        name: str = "",
        program: List[int],
        input_callback: Optional[Callable] = None,
        output_callback: Optional[Callable] = None,
    ) -> None:
        self.name = name
        self.is_halted = False
        self.program = {}
        for index, integer in enumerate(program):
            self.program[index] = integer
        self.index = 0
        self.relative_base = 0
        self.input_callback = input_callback
        self.output_callback = output_callback

    def get_next(self, parameter_mode: ParameterMode, *, address: bool = False) -> int:
        value = self.peek_next(parameter_mode=parameter_mode, address=address)
        self.index += 1
        return value

    def peek_next(self, parameter_mode: ParameterMode, *, address: bool = False) -> int:
        if address:
            value = self.get_value(self.index)

            if parameter_mode == ParameterMode.IMMEDIATE:
                raise Exception("Cannot use immediate in address mode")

            if parameter_mode == ParameterMode.POSITION:
                return value

            if parameter_mode == ParameterMode.RELATIVE:
                return self.relative_base + value

        else:
            value = self.get_value(self.index)

            if parameter_mode == ParameterMode.IMMEDIATE:
                return value

            if parameter_mode == ParameterMode.POSITION:
                return self.get_value(value)

            if parameter_mode == ParameterMode.RELATIVE:
                return self.get_value(self.relative_base + value)

        raise Exception()

    def peek_next_instruction(self) -> Opcode:
        value = self.get_value(self.index)
        opcode, _ = Computer.opcode_parameters(value)
        return opcode

    def get_value(self, index: int) -> int:
        assert index >= 0
        if index not in self.program:
            self.program[index] = 0
        return self.program[index]

    def set_value(self, value: int, index: int) -> None:
        self.program[index] = value

    def state(self) -> str:
        counter = 0
        output = []
        while True:
            if counter not in self.program:
                break
            output.append(self.program[counter])
            counter += 1
        return ",".join(map(str, output))

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

        defaults = {
            Opcode.ADD: [
                ParameterMode.POSITION,
                ParameterMode.POSITION,
                ParameterMode.POSITION,
            ],
            Opcode.MULTIPLY: [
                ParameterMode.POSITION,
                ParameterMode.POSITION,
                ParameterMode.POSITION,
            ],
            Opcode.INPUT: [ParameterMode.POSITION],
            Opcode.OUTPUT: [ParameterMode.POSITION],
            Opcode.JUMP_IF_TRUE: [ParameterMode.POSITION, ParameterMode.POSITION],
            Opcode.JUMP_IF_FALSE: [ParameterMode.POSITION, ParameterMode.POSITION],
            Opcode.LESS_THAN: [
                ParameterMode.POSITION,
                ParameterMode.POSITION,
                ParameterMode.POSITION,
            ],
            Opcode.EQUALS: [
                ParameterMode.POSITION,
                ParameterMode.POSITION,
                ParameterMode.POSITION,
            ],
            Opcode.RELATIVE_BASE_OFFSET: [ParameterMode.POSITION],
            Opcode.HALT: [],
        }

        default_modes = defaults[opcode]
        for index, mode in enumerate(parameter_modes):
            default_modes[index] = mode

        return opcode, default_modes

    def do_next(self) -> Opcode:
        if self.is_halted:
            return Opcode.HALT

        instruction_value = self.get_next(ParameterMode.IMMEDIATE)

        opcode, parameter_modes = Computer.opcode_parameters(instruction_value)

        if opcode == Opcode.ADD:
            value1 = self.get_next(parameter_modes[0])
            value2 = self.get_next(parameter_modes[1])
            output_index = self.get_next(parameter_modes[2], address=True)
            output_value = value1 + value2
            self.set_value(output_value, output_index)
            return opcode

        if opcode == Opcode.MULTIPLY:
            value1 = self.get_next(parameter_modes[0])
            value2 = self.get_next(parameter_modes[1])
            output_index = self.get_next(parameter_modes[2], address=True)
            output_value = value1 * value2
            self.set_value(output_value, output_index)
            return opcode

        if opcode == Opcode.INPUT:
            assert self.input_callback is not None
            value = self.input_callback(self.name)
            assert isinstance(value, int)
            output_index = self.get_next(parameter_modes[0], address=True)
            self.set_value(value, output_index)
            return opcode

        if opcode == Opcode.OUTPUT:
            value1 = self.get_next(parameter_modes[0])
            if self.output_callback:
                self.output_callback(self.name, value1)
            else:
                print(f"OUTPUT: {value1}")
            return opcode

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
            output_index = self.get_next(parameter_modes[2], address=True)
            if value1 < value2:
                self.set_value(1, output_index)
            else:
                self.set_value(0, output_index)
            return opcode

        if opcode == Opcode.EQUALS:
            value1 = self.get_next(parameter_modes[0])
            value2 = self.get_next(parameter_modes[1])
            output_index = self.get_next(parameter_modes[2], address=True)
            if value1 == value2:
                self.set_value(1, output_index)
            else:
                self.set_value(0, output_index)
            return opcode

        if opcode == Opcode.RELATIVE_BASE_OFFSET:
            value1 = self.get_next(parameter_modes[0])
            self.relative_base += value1
            return opcode

        if opcode == Opcode.HALT:
            self.is_halted = True
            raise HaltException()

        assert False, "Never should reach here"

    def try_do_next(self) -> Opcode:
        try:
            return self.do_next()
        except HaltException:
            return Opcode.HALT

    def run(self) -> None:

        try:
            while self.do_next() != Opcode.HALT:
                pass
        except HaltException:
            pass

    def halt(self) -> None:
        self.is_halted = True
