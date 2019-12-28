from typing import List, Tuple

import intcode

class Camera:

    output: List[List[str]]
    current_row: List[str]
    intersections: List[Tuple[int, int]]
    computer: intcode.Computer

    def __init__(self, input_values: List[int]) -> None:
        self.computer = intcode.Computer(program=input_values)
        self.computer.output_callback = self.render_character
        self.output = []
        self.current_row = []
        self.intersections = []

    def run(self) -> int:
        self.computer.run()

        for row in self.output:
            for character in row:
                print(character, sep='', end='')
            print("\n", sep='', end='')

        for y in range(len(self.output)):
            for x in range(len(self.output[y])):
                if self.output[y][x] == "#":
                    try:
                        neighbors = ""
                        neighbors += self.output[y][x-1]
                        neighbors += self.output[y][x+1]
                        neighbors += self.output[y-1][x]
                        neighbors += self.output[y+1][x]
                        if neighbors == "####":
                            self.intersections.append((x, y))
                    except:
                        continue

        total = 0
        for x, y in self.intersections:
            total += x * y

        return total

    def render_character(self, name: str, value: int) -> None:
        character = chr(value)
        if character != "\n":
            self.current_row.append(character)
        else:
            self.output.append(self.current_row)
            self.current_row = []

def part1(input_values) -> None:
    camera = Camera(input_values)
    print("Part 1:", camera.run())

def part2(input_values) -> None:
    pass


with open("year_2019/input_17.txt") as input_file:
    contents = input_file.read()

input_values = list(map(int, contents.split(",")))

part1(input_values)
#part2(input_values)