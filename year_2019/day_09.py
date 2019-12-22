import itertools
from typing import List, Tuple

import intcode

with open("year_2019/input_09.txt") as input_file:
    contents = input_file.read()

input_values = list(map(int, contents.split(",")))

def part1():
    computer = intcode.Computer(program=input_values)
    computer.input_callback = intcode.input_list_wrapper([1])
    computer.run()

def part2():
    computer = intcode.Computer(program=input_values)
    computer.input_callback = intcode.input_list_wrapper([2])
    computer.run()

part1()
part2()