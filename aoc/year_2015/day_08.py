with open("year_2015/input_08.txt") as f:
    contents = f.read()


def part1():
    total_code = 0
    total_characters = 0

    for line in contents.splitlines():
        code_count = 2
        line = line[1:-1]

        i = -1
        while True:
            i += 1
            if i >= len(line) - 1:
                break

            c = line[i]
            if c != "\\":
                continue

            # We know that we've hit an escape sequence here
            if line[i + 1] in ['"', "\\"]:
                line = line[:i] + line[i + 1 :]
                code_count += 1
                continue

            if line[i + 1] == "x":
                line = line[:i] + "#" + line[i + 3 :]
                code_count += 3
                continue

        character_count = len(line)

        total_characters += character_count
        total_code += character_count + code_count

    print("Part 1:", total_code - total_characters)


def part2():
    diff = 0

    for line in contents.splitlines():
        original_line = line[:]

        i = -1
        while True:
            i += 1
            if i >= len(line):
                break

            c = line[i]
            if c in ['"', "\\"]:
                line = line[:i] + "\\" + line[i:]
                i += 1
                continue

        line = f'"{line}"'

        character_count = len(line)
        code_count = len(original_line)

        diff += len(line) - len(original_line)

    print("Part 2:", diff)


part1()
part2()
