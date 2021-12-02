import collections
import re
import string


with open("year_2016/input_04.txt") as f:
    contents = f.readlines()

def parse_entries():
    pattern = re.compile("([a-z\-]*)-(\d*)\[([a-z]*)\]")

    output = []

    for line in contents:
        line = line.strip()
        match = pattern.match(line)
        assert match
        name = match.group(1)
        sector_id = int(match.group(2))
        checksum = match.group(3)

        output.append((name, sector_id, checksum))

    return output


def validate_entry(name, sector_id, checksum):
    
    counter = collections.Counter()
    name = name.replace("-", "")
    counter.update(name)

    count_list = []

    for key in set(counter.elements()):
        value = counter[key]
        count_list.append((key, value))

    count_list.sort(key=lambda x: (x[1], ord('z') - ord(x[0])), reverse=True)

    calculated_checksum = ""
    for letter, _ in count_list[:5]:
        calculated_checksum += letter

    return calculated_checksum == checksum


def rot_encode(value, n):
    lookup = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[n:] + string.ascii_lowercase[:n]
    )

    return value.translate(lookup)


def part1():

    entries = parse_entries()

    total = 0
    for name, sector_id, checksum in entries:
        if validate_entry(name, sector_id, checksum):
            total += sector_id

    return total


def part2():

    entries = parse_entries()

    for name, sector_id, checksum in entries:
        if not validate_entry(name, sector_id, checksum):
            continue

        decoded = rot_encode(name, sector_id % 26)
        if decoded == "northpole-object-storage":
            return sector_id

    return None

print("Part 1:", part1())
print("Part 2:", part2())
