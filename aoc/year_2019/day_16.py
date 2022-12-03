from itertools import accumulate, islice
import math
from typing import Iterator, List

BASE_PATTERN = [0, 1, 0, -1]


def generate_pattern(count, offset) -> Iterator[int]:
    index = math.floor(offset / count)
    offset_remainder = offset - (index * 4) + 1
    while True:
        index = index % 4
        for _ in range(offset_remainder, count):
            yield BASE_PATTERN[index]
        offset_remainder = 0
        index += 1


def run_pass(input_values: List[int]) -> List[int]:
    for pass_index in range(0, len(input_values)):
        pairs = zip(
            input_values[pass_index:], generate_pattern(pass_index + 1, pass_index)
        )
        total = 0
        outputs = []
        for a, b in pairs:
            outputs.append(f"{a}*{b:<2}")
            total += a * b
        result = abs(total) % 10
        # print(" + ".join(outputs) + f" = {result}")
        yield result


with open("year_2019/input_16.txt", encoding="utf-8") as input_file:
    contents = input_file.read().strip()

all_input_values = list(map(int, [character for character in contents]))

# Part 1
values = all_input_values[:]
for i in range(0, 100):
    values = list(run_pass(values))
print("Part 1:", "".join(map(str, values[:8])))


# Part 2
all_input_values = all_input_values * 10_000
values = list(reversed(all_input_values))
offset = int("".join(map(str, all_input_values[:7])))

for i in range(0, 100):
    values = list(
        islice(
            accumulate(values, lambda a, b: (a + b) % 10), len(all_input_values) - offset
        )
    )

print("Part 2:", "".join(map(str, list(reversed(values))[:8])))
