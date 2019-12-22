import itertools
from typing import List, Tuple


def count_digits(layer: List[List[int]], digit: int) -> int:
    count = 0
    for row in layer:
        for pixel in row:
            if pixel == digit:
                count += 1
    return count


with open("year_2019/input_08.txt") as input_file:
    contents = input_file.read().strip()

WIDTH = 25
HEIGHT = 6

values = list(map(int, contents))

layers = []

while True:
    layer = []

    for _ in range(0, HEIGHT):
        row = []
        for _ in range(0, WIDTH):
            row.append(values.pop(0))
        layer.append(row)

    layers.append(layer)

    if len(values) == 0:
        break

min_count = WIDTH * HEIGHT
min_layer = None

for layer in layers:
    count = count_digits(layer, 0)
    if count < min_count:
        min_count = count
        min_layer = layer

print(count_digits(min_layer, 1) * count_digits(min_layer, 2))

