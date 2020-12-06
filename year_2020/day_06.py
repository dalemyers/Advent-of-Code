from shared import read_file_lines

contents = read_file_lines("year_2020/input_06.txt")


def get_groups():
    groups = []
    buffer = []
    for line in contents:
        if len(line) == 0:
            groups.append(buffer)
            buffer = []
        else:
            buffer.append(line)

    groups.append(buffer)

    return groups


def part1():
    groups = get_groups()
    total = 0
    for group in groups:
        answers = set()
        for person in group:
            for character in person:
                answers.add(character)

        total += len(answers)

    return total


def part2():
    groups = get_groups()
    total = 0
    for group in groups:
        answers = {}
        for person in group:
            for character in person:
                if character not in answers:
                    answers[character] = 0
                answers[character] += 1
        for key, value in answers.items():
            if value == len(group):
                total += 1

    return total


print("Part 1:", part1())
print("Part 2:", part2())
