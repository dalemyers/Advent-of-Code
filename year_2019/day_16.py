import math
from typing import Any, List

def rotate_list(input_list: List[Any], by_count: int) -> List[Any]:
    return input_list[by_count:] + input_list[:by_count]

def rotate_left(input_list: List[Any]) -> List[Any]:
    return rotate_list(input_list, 1)

def rotate_right(input_list: List[Any]) -> List[Any]:
    return rotate_list(input_list, -1)


BASE_PATTERN = [0, 1, 0, -1]

def run_pass(input_values: List[int]) -> List:
    output = []

    for pass_index in range(0, len(input_values)):

        pattern = []
        for element in BASE_PATTERN:
            for i in range(0, pass_index + 1):
                pattern.append(element)

        extended_pattern = pattern * math.ceil(len(input_values) / len(pattern))
        extended_pattern = extended_pattern[1:]

        pairs = zip(input_values, extended_pattern)
        total = 0
        for a, b in pairs:
            total += a * b
        result = abs(total) % 10
        output.append(result)

    return output

with open("year_2019/input_16.txt") as input_file:
    contents = input_file.read().strip()

input_values = list(map(int, [character for character in contents]))


values = input_values[:]
for i in range(0, 100):
    values = run_pass(values[:])
    print("".join(map(str, values[:8])))



