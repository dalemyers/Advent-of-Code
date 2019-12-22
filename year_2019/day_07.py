import itertools
from typing import List, Tuple

import intcode

with open("year_2019/input_07.txt") as input_file:
    contents = input_file.read()

input_values = list(map(int, contents.split(",")))

def run_amplifier(inputs: List[int], loop_back: bool = False) -> int:

    ampA = intcode.Computer(name='a', program=input_values)
    ampB = intcode.Computer(name='b', program=input_values)
    ampC = intcode.Computer(name='c', program=input_values)
    ampD = intcode.Computer(name='d', program=input_values)
    ampE = intcode.Computer(name='e', program=input_values)

    data_map = {'a': [inputs[0], 0], 'b': [inputs[1]], 'c': [inputs[2]], 'd': [inputs[3]], 'e': [inputs[4]]}

    def append(key, value):
        data_map[key].append(value)

    ampA.output_callback = lambda name, value: append('b', value)
    ampB.output_callback = lambda name, value: append('c', value)
    ampC.output_callback = lambda name, value: append('d', value)
    ampD.output_callback = lambda name, value: append('e', value)
    ampE.output_callback = lambda name, value: append('a', value)

    ampA.input_callback = lambda name: data_map[name].pop(0)
    ampB.input_callback = lambda name: data_map[name].pop(0)
    ampC.input_callback = lambda name: data_map[name].pop(0)
    ampD.input_callback = lambda name: data_map[name].pop(0)
    ampE.input_callback = lambda name: data_map[name].pop(0)

    iterations = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

    def run_as_far_as_possible(amplifier: intcode.Computer) -> None:
        while True:
            if amplifier.is_halted:
                break

            op_code, _ = intcode.Computer.opcode_parameters(amplifier.peek_next())

            if op_code == intcode.Opcode.INPUT and len(data_map[amplifier.name]) == 0:
                break

            op_code = amplifier.try_do_next()
            iterations[amplifier.name] += 1

            if op_code in [intcode.Opcode.HALT]:
                break

    while True:

        run_as_far_as_possible(ampA)
        run_as_far_as_possible(ampB)
        run_as_far_as_possible(ampC)
        run_as_far_as_possible(ampD)
        run_as_far_as_possible(ampE)

        if not loop_back:
            break

        if all([ampA.is_halted, ampB.is_halted, ampC.is_halted, ampD.is_halted, ampE.is_halted]):
            break

    return data_map['a'][0]

def run_options(options, loop_back) -> Tuple[int, List[int]]:
    max_output = 0
    max_index = 0
    for sequence in itertools.permutations(options): 
        output = run_amplifier(list(sequence), loop_back)
        if output > max_output:
            max_output = output
            max_index = sequence
    return (max_output, max_index)


print("Part 1:", run_options([0, 1, 2, 3, 4], False))
print("Part 2:", run_options([5, 6, 7, 8, 9], True))
