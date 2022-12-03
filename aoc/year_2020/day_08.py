from shared import read_file_lines

contents = read_file_lines("year_2020/input_08.txt")
base_instructions = [(i.split(" ")[0], int(i.split(" ")[1])) for i in contents]


def run_instructions(instructions):
    accumulator = 0
    pc = 0
    visited = set()
    while True:
        if pc >= len(instructions):
            return True, accumulator

        if pc in visited:
            return False, accumulator

        visited.add(pc)

        instruction, argument = instructions[pc]
        if instruction == "acc":
            accumulator += argument
            pc += 1
            continue

        if instruction == "jmp":
            pc += argument
            continue

        if instruction == "nop":
            pc += 1
            continue


def part1():
    return run_instructions(base_instructions)[1]


def part2():
    instruction_lookup = {"jmp": "nop", "nop": "jmp"}

    for i in range(len(base_instructions)):
        if base_instructions[i][0] not in ["nop", "jmp"]:
            continue
        new_instructions = base_instructions[:]
        new_instruction = instruction_lookup[base_instructions[i][0]]
        new_instructions[i] = (new_instruction, base_instructions[i][1])
        result, acc = run_instructions(new_instructions)
        if result:
            return acc


print("Part 1:", part1())
print("Part 2:", part2())
