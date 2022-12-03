import re

with open("year_2015/input_23.txt") as f:
    contents = f.readlines()

"""
hlf a
inc a
inc b
jie a, +4
jio a, +22
jio a, +8
jmp -7
jmp +19
jmp +2
tpl a
"""


class Computer:
    def __init__(self, a_init=0, b_init=0):
        self.registers = {"a": a_init, "b": b_init}

    def run_instruction(self, instruction, arguments):
        if instruction == "hlf":
            self.registers[arguments[0]] /= 2
        elif instruction == "tpl":
            self.registers[arguments[0]] *= 3
        elif instruction == "inc":
            self.registers[arguments[0]] += 1
        elif instruction == "jmp":
            return arguments[0]
        elif instruction == "jie":
            if self.registers[arguments[0]] % 2 == 0:
                return arguments[1]
        elif instruction == "jio":
            if self.registers[arguments[0]] == 1:
                return arguments[1]
        return 1


def get_instructions():
    output = []
    pattern = re.compile(r"([a-z]*) ([^,]*)(?:, ([+\-]\d*))?")
    for line in contents:
        line = line.strip()
        match = pattern.match(line)
        assert match
        instruction = match.group(1)
        raw_args = [match.group(2)]
        if match.group(3):
            raw_args.append(match.group(3))
        args = []
        for arg in raw_args:
            if arg.startswith("+") or arg.startswith("-"):
                args.append(int(arg))
            else:
                args.append(arg)
        output.append((instruction, args))
    return output


def part1():
    instructions = get_instructions()
    computer = Computer()
    pc = 0

    while True:
        if pc >= len(instructions):
            break

        instruction, args = instructions[pc]
        offset = computer.run_instruction(instruction, args)
        pc += offset

    return computer.registers["b"]


def part2():
    instructions = get_instructions()
    computer = Computer(1)
    pc = 0

    while True:
        if pc >= len(instructions):
            break

        instruction, args = instructions[pc]
        offset = computer.run_instruction(instruction, args)
        pc += offset

    return computer.registers["b"]


print("Part 1:", part1())
print("Part 2:", part2())
