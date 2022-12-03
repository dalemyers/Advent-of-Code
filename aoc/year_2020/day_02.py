import re

with open("year_2020/input_02.txt", encoding="utf-8") as input_file:
    contents = input_file.readlines()

contents = [c.strip() for c in contents]


def count(letter, string):
    counter = 0
    for character in string:
        if character == letter:
            counter += 1
    return counter


def part1():
    # Sample
    # 5-16 j: jjjjkjjzjjjjjfjzjj
    pattern = re.compile(r"(\d*)-(\d*) (.): (.*)")
    valid_passwords = 0
    for line in contents:
        match = pattern.match(line)
        if not match:
            continue
        minimum = int(match.group(1))
        maximum = int(match.group(2))
        letter = match.group(3)
        password = match.group(4)
        occurences = count(letter, password)
        if minimum <= occurences <= maximum:
            valid_passwords += 1
    return valid_passwords


def part2():
    # Sample
    # 5-16 j: jjjjkjjzjjjjjfjzjj
    pattern = re.compile(r"(\d*)-(\d*) (.): (.*)")
    valid_passwords = 0
    for line in contents:
        match = pattern.match(line)
        if not match:
            continue
        p1 = int(match.group(1)) - 1
        p2 = int(match.group(2)) - 1
        letter = match.group(3)
        password = match.group(4)
        if (password[p1] == letter or password[p2] == letter) and password[
            p1
        ] != password[p2]:
            valid_passwords += 1
    return valid_passwords


print("Part 1:", part1())
print("Part 2:", part2())
