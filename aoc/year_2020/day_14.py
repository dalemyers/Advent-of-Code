import copy
import enum
from shared import read_file_lines

contents = read_file_lines("year_2020/input_14.txt")


def mask1(value, bit_mask):
    binary_value = bin(int(value))[2:].zfill(36)
    output = ""
    for v, b in zip(binary_value, bit_mask):
        if b in ["0", "1"]:
            output += b
        else:
            output += v
    return output


def mask2(value, bit_mask):
    binary_value = bin(int(value))[2:].zfill(36)
    output = ""
    for v, b in zip(binary_value, bit_mask):
        if b == "0":
            output += v
        elif b == "1":
            output += "1"
        else:
            output += "x"
    return output


def generate_addresses(address):
    characters = len([c for c in address if c == "x"])
    replacement = [0] * characters

    while True:
        output = ""
        index = 0
        for character in address:
            if character in ["1", "0"]:
                output += character
            else:
                output += str(replacement[index])
                index += 1
        yield output
        replacement_value = int("".join(map(str, replacement)), 2)
        replacement_value += 1
        replacement_string = bin(replacement_value)[2:].zfill(characters)
        replacement = list(map(int, replacement_string))

        if len(replacement) > characters:
            return


def part1():
    bit_mask = "x" * 36
    memory = {}
    for line in contents:
        components = line.split(" = ")
        if components[0] == "mask":
            bit_mask = components[1]
        else:
            # mem[12345]
            assert components[0].startswith("mem[")
            memory_address = int(components[0][4:-1])
            memory[memory_address] = mask1(components[1], bit_mask)

    total = 0
    for value in memory.values():
        total += int(value, 2)

    return total


def part2():
    bit_mask = "x" * 36
    memory = {}
    for line in contents:
        components = line.split(" = ")
        if components[0] == "mask":
            bit_mask = components[1]
        else:
            # mem[12345]
            assert components[0].startswith("mem[")
            memory_address = int(components[0][4:-1])
            masked_address = mask2(memory_address, bit_mask)
            for address in generate_addresses(masked_address):
                memory[address] = int(components[1])

    total = 0
    for value in memory.values():
        total += value

    return total


print("Part 1:", part1())
print("Part 2:", part2())
