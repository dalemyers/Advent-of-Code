import enum
from typing import List


WIDTH = 25
HEIGHT = 6


class Color(enum.Enum):
    BLACK = 0
    WHITE = 1
    TRANSPARENT = 2


def count_colors(layer: List[List[Color]], color: Color) -> int:
    count = 0
    for row in layer:
        for pixel in row:
            if pixel == color:
                count += 1
    return count


def generate_layers(values):
    layers = []

    while True:
        layer = []

        for _ in range(0, HEIGHT):
            row = []
            for _ in range(0, WIDTH):
                row.append(Color(values.pop(0)))
            layer.append(row)

        layers.append(layer)

        if len(values) == 0:
            break

    return layers


def part1():
    min_count = WIDTH * HEIGHT
    min_layer = None

    for layer in layers:
        count = count_colors(layer, Color.BLACK)
        if count < min_count:
            min_count = count
            min_layer = layer

    return count_colors(min_layer, Color.WHITE) * count_colors(
        min_layer, Color.TRANSPARENT
    )


def flatten_layers(layers):

    output = []

    for y in range(0, HEIGHT):
        row = []
        for x in range(0, WIDTH):
            for layer in layers:
                if layer[y][x] == Color.TRANSPARENT:
                    continue
                row.append(layer[y][x])
                break
        output.append(row)

    return output


def render_image(image):
    for row in image:
        for pixel in row:
            if pixel == Color.WHITE:
                print(" ", sep="", end="")
            else:
                print("#", sep="", end="")
        print("\n", sep="", end="")


with open("year_2019/input_08.txt", encoding="utf-8") as input_file:
    contents = input_file.read().strip()

values = list(map(int, contents))
all_layers = generate_layers(values)

print("Part 1:", part1())

full_image = flatten_layers(all_layers)
print("Part 2:")
render_image(full_image)
print()
