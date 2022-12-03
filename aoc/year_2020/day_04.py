from shared import is_int

FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
]


def get_passport(raw_data):
    raw_data = "\n".join(raw_data)
    raw_data = raw_data.replace(" ", "\n")
    fields = {}
    for field in raw_data.split("\n"):
        name, value = field.split(":")
        fields[name] = value
    return fields


def get_passports(raw_data):

    buffer = []
    passports = []
    for line in raw_data.split("\n"):
        if line.strip() == "":
            passports.append(get_passport(buffer))
            buffer = []
        else:
            buffer.append(line)

    if len(buffer) > 0:
        passports.append(get_passport(buffer))

    return passports


with open("year_2020/input_04.txt", encoding="utf-8") as input_file:
    contents = input_file.read()


def part1():
    passports = get_passports(contents)
    count = 0

    for passport in passports:
        is_valid = True
        for field in FIELDS:
            if field not in passport:
                is_valid = False
                break

        if is_valid:
            count += 1

    return count


def validate_year(value, min_year, max_year):
    if not value:
        return False

    if len(value) != 4:
        return False

    if not is_int(value):
        return False

    if int(value) < min_year:
        return False

    if int(value) > max_year:
        return False

    return True


def validate_height(value):

    if not value:
        return False

    unit = value[-2:]
    value = value[:-2]
    if unit not in ["cm", "in"]:
        return False

    if not is_int(value):
        return False

    value = int(value)

    if unit == "cm":
        if value < 150 or value > 193:
            return False

    if unit == "in":
        if value < 59 or value > 76:
            return False

    return True


def validate_haircolor(value):

    if not value:
        return False

    if len(value) != 7:
        return False

    if value[0] != "#":
        return False

    for character in value[1:]:
        if character not in "abcdef0123456789":
            return False

    return True


def validate_eyecolor(value):

    if not value:
        return False

    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_passportid(value):

    if not value:
        return False

    if len(value) != 9:
        return False

    return is_int(value)


def part2():
    passports = get_passports(contents)
    count = 0

    for passport in passports:
        is_valid = True

        if not validate_year(passport.get("byr"), 1920, 2002):
            continue

        if not validate_year(passport.get("iyr"), 2010, 2020):
            continue

        if not validate_year(passport.get("eyr"), 2020, 2030):
            continue

        if not validate_height(passport.get("hgt")):
            continue

        if not validate_haircolor(passport.get("hcl")):
            continue

        if not validate_eyecolor(passport.get("ecl")):
            continue

        if not validate_passportid(passport.get("pid")):
            continue

        count += 1

    return count


print("Part 1:", part1())
print("Part 2:", part2())
