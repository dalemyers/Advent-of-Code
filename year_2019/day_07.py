from typing import List

import intcode

with open("year_2019/input_07.txt") as input_file:
    contents = input_file.read()

input_values = list(map(int, contents.split(",")))

def run_amplifier(inputs: List[int]) -> int:
    outputs = []

    ampA = intcode.Program(input_values, intcode.input_list_wrapper([inputs[0], 0]), outputs.append)
    ampA.run()

    ampB = intcode.Program(input_values, intcode.input_list_wrapper([inputs[1], outputs[-1]]), outputs.append)
    ampB.run()

    ampC = intcode.Program(input_values, intcode.input_list_wrapper([inputs[2], outputs[-1]]), outputs.append)
    ampC.run()

    ampD = intcode.Program(input_values, intcode.input_list_wrapper([inputs[3], outputs[-1]]), outputs.append)
    ampD.run()

    ampE = intcode.Program(input_values, intcode.input_list_wrapper([inputs[4], outputs[-1]]), outputs.append)
    ampE.run()

    return outputs[-1]

max_output = 0
max_index = 0
for a in range(0, 5):
    for b in range(0, 5):
        for c in range(0, 5):
            for d in range(0, 5):
                for e in range(0, 5):
                    if a in [b, c, d, e]:
                        continue
                    if b in [c, d, e]:
                        continue
                    if c in [d, e]:
                        continue
                    if d == e:
                        continue
                    sequence = [a, b, c, d, e]
                    #print(sequence)
                    output = run_amplifier(sequence)
                    if output > max_output:
                        print(output, max_output, sequence)
                        max_output = output
                        max_index = sequence

print(max_output, max_index)