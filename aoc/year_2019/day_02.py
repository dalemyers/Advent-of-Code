import intcode

with open("year_2019/input_02.txt", encoding="utf-8") as f:
    full_input = f.read().strip()


def part1():
    computer = intcode.Computer(program=list(map(int, full_input.split(","))))
    computer.set_value(12, 1)
    computer.set_value(2, 2)
    computer.run()
    print("Part 1:", computer.get_value(0))


def run_program(noun: int, verb: int) -> int:
    computer = intcode.Computer(program=list(map(int, full_input.split(","))))
    computer.set_value(noun, 1)
    computer.set_value(verb, 2)
    computer.run()
    return computer.get_value(0)


def part2():
    found_noun = None
    found_verb = None

    for noun in range(0, 100):
        for verb in range(0, 100):
            result = run_program(noun, verb)
            if result == 19690720:
                found_noun = noun
                found_verb = verb
                break

        if found_noun is not None:
            break

    print("Part 2:", 100 * found_noun + found_verb)


part1()
part2()
