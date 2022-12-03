import enum
import re


class SequenceType(enum.Enum):

    normal = 1
    hypernet = 2


with open("year_2016/input_07.txt") as f:
    contents = f.readlines()
contents = [c.strip() for c in contents]


def parse_ip(raw_ip):
    sequences = []
    buffer = ""
    current_sequence = SequenceType.normal
    for character in raw_ip:
        flush = False
        next_sequence = SequenceType.normal
        if character == "[":
            flush = True
            next_sequence = SequenceType.hypernet
        elif character == "]":
            flush = True
            next_sequence = SequenceType.normal
        else:
            buffer += character

        if flush:
            sequences.append((buffer, current_sequence))
            buffer = ""
            current_sequence = next_sequence

    sequences.append((buffer, current_sequence))
    buffer = ""

    sequences = [
        (sequence, sequence_type) for sequence, sequence_type in sequences if len(sequence) > 0
    ]

    return sequences


def get_ips():
    ips = []

    for raw_ip in contents:
        ips.append(parse_ip(raw_ip))

    return ips


def check_abba(string):
    for i in range(0, len(string) - 3):
        subsequence1 = string[i : i + 2]
        subsequence2 = string[i + 2 : i + 4]
        if string[i] == string[i + 1]:
            continue
        if subsequence1 == subsequence2[::-1]:
            return True
    return False


def find_abas(value):
    pattern = re.compile(r"(?=(.)(.)\1)")

    results = []

    for match in pattern.finditer(value):
        results.append((match.groups(), match.span()))

    return results


def has_ssl(ip):
    normals = [sequence for sequence, sequence_type in ip if sequence_type == SequenceType.normal]
    hypernets = [
        sequence for sequence, sequence_type in ip if sequence_type == SequenceType.hypernet
    ]

    is_invalid = False

    for sequence in normals:
        locations = find_abas(sequence)

        found = False
        has_pattern = False

        for pattern, span in locations:
            if pattern[0] == pattern[1]:
                continue

            # Reversed pattern
            new_pattern = pattern[1] + pattern[0] + pattern[1]

            for hseq in hypernets:
                if new_pattern in hseq:
                    return True

    return False


def part1():
    ips = get_ips()

    count = 0

    for ip in ips:
        has_tls = False
        for sequence, sequence_type in ip:
            if sequence_type == SequenceType.normal:
                if check_abba(sequence):
                    has_tls = True
            else:
                if check_abba(sequence):
                    has_tls = False
                    break

        if has_tls:
            count += 1

    return count


def part2():
    ips = get_ips()

    count = 0

    for ip in ips:
        if has_ssl(ip):
            count += 1

    return count


print("Part 1:", part1())
print("Part 2:", part2())
