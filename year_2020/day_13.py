import copy
import enum
from shared import read_file_lines

contents = read_file_lines("year_2020/input_13.txt")



def part1():
    earliest_departure = int(contents[0])
    buses = sorted([int(c) for c in contents[1].split(",") if c != "x"])
    waits = []
    for index, bus in enumerate(buses):
        departures = earliest_departure // bus
        wait_time = ((departures + 1) * bus) - earliest_departure
        waits.append((wait_time, bus))

    quickest = min(waits, key=lambda x: x[0])
    return quickest[0] * quickest[1]

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solve_for_buses(index, a, a_offset, b, b_offset):
    factor = 0
    while True:
        factor += 1
        a_result = a * factor + a_offset
        for b_fact in range(1, b):
            b_result = b * b_fact - b_offset
            if b_result > a_result:
                break
            if b_result == a_result:
                return factor, b_fact



def part2():
    buses = [int(c) if c != "x" else -1 for c in contents[1].split(",")]
    offsets = sorted([(c, offset) for (offset, c) in enumerate(buses) if c != -1], key=lambda x:x[0])

    increment_by = offsets[0][0]
    offsets = offsets[1:]
    timestamp = 0

    for bus, offset in offsets:
        current_offset = None
        while True:
            if (timestamp + offset) % bus == 0:
                if current_offset is None:
                    current_offset = timestamp
                else:
                    increment_by = timestamp - current_offset
                    break

            timestamp += increment_by

    return current_offset

print("Part 1:", part1())
print("Part 2:", part2())
