import json

from shared import is_int


with open("year_2015/input_12.txt") as f:
    input_data = json.load(f)


def part1():
    def calc_dictionary(data):
        total = 0
        for k, v in data.items():
            if is_int(k):
                total += int(k)
            if is_int(v):
                total += int(v)
            else:
                total += calc(v)
        return total

    def calc_array(data):
        total = 0
        for value in data:
            total += calc(value)
        return total

    def calc(data):
        if is_int(data):
            return int(data)
        elif isinstance(data, list):
            return calc_array(data)
        elif isinstance(data, dict):
            return calc_dictionary(data)
        else:
            return 0

    return calc(input_data)


def part2():
    class RedException(Exception):
        pass

    def calc_dictionary(data):
        total = 0
        for k, v in data.items():
            if is_int(k):
                total += int(k)
            if k == "red":
                raise RedException()
            if v == "red":
                raise RedException()
            if is_int(v):
                total += int(v)
            else:
                total += calc(v)
        return total

    def calc_array(data):
        total = 0
        for value in data:
            total += calc(value)
        return total

    def calc(data):
        if is_int(data):
            return int(data)

        try:
            if isinstance(data, list):
                return calc_array(data)
            elif isinstance(data, dict):
                return calc_dictionary(data)
            else:
                return 0
        except RedException:
            return 0

    return calc(input_data)


print("Part 1:", part1())
print("Part 2:", part2())
