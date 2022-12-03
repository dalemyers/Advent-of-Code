import enum
from shared import read_file_lines, create_bool_grid, render_bw_grid

contents = read_file_lines("year_2016/input_09.txt")
contents = contents[0].strip()


def decompress1(data):
    output = ""
    index = -1
    while True:
        index += 1
        if index >= len(data):
            break

        character = data[index]
        if character != "(":
            output += character
            continue

        buffer = ""
        while True:
            index += 1
            next_character = data[index]
            if next_character == ")":
                index += 1
                break
            else:
                buffer += next_character

        number_of_characters, count = list(map(int, buffer.split("x")))

        character_pattern = data[index : index + number_of_characters]

        for _ in range(count):
            output += character_pattern

        index += number_of_characters - 1

    return output


class Marker:
    def __init__(self, pattern, sequence, count):
        self.sequence = sequence
        self.count = count
        self.length = len(pattern) + 2


def decompress2(data):

    index = -1
    while True:
        index += 1
        if index >= len(data):
            break

        character = data[index]
        if character != "(":
            data = data[:index] + character + data[index + 1 :]
            continue

        buffer = ""
        start_index = index
        while True:
            index += 1
            next_character = data[index]
            if next_character != ")":
                buffer += next_character
                continue

            index += 1
            number_of_characters, count = list(map(int, buffer.split("x")))
            character_pattern = data[index : index + number_of_characters]
            expanded = character_pattern * count
            data = (
                data[:start_index]
                + expanded
                + data[start_index + len(buffer) + 2 + number_of_characters :]
            )
            index = start_index - 1

            break

    print(data)
    return data


def decompress3(data) -> int:

    index = -1
    total = 0
    while True:
        index += 1
        if index >= len(data):
            break

        character = data[index]
        if character != "(":
            total += 1
            continue

        buffer = ""
        start_index = index
        while True:
            index += 1
            next_character = data[index]
            if next_character != ")":
                buffer += next_character
                continue

            index += 1
            number_of_characters, count = list(map(int, buffer.split("x")))
            character_pattern = data[index : index + number_of_characters]
            expanded_count = decompress3(character_pattern * count)
            total += expanded_count
            index = start_index + len(buffer) + 2 + number_of_characters - 1
            break

    return total


def decompress4(data) -> int:

    index = 0
    total = 0

    while index < len(data):
        character = data[index]

        if character != "(":
            total += 1
            index += 1
            continue

        buffer = ""
        index += 1
        character = data[index]
        while character != ")":
            buffer += character
            index += 1
            character = data[index]
        index += 1

        number_of_characters, count = list(map(int, buffer.split("x")))
        character_pattern = data[index : index + number_of_characters]
        index += number_of_characters
        total += decompress4(character_pattern * count)

    return total


def part1():
    return len(decompress1(contents))


def part2():
    # While all attempts here work, even v4 is super slow taking > an hour to run.
    # This needs to be optimised somehow.
    assert decompress4("(3x3)XYZ") == 9
    assert decompress4("X(8x2)(3x3)ABCY") == 20
    assert decompress4("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 241920
    assert decompress4("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN") == 445
    return decompress4(contents)


print("Part 1:", part1())
print("Part 2:", part2())
