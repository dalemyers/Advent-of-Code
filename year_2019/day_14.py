import collections
import math
from typing import Dict, List, Optional, Tuple


class Material:

    def __init__(self, name: str, count: int) -> None:
        self.name = name
        self.count = count

    def __repr__(self) -> str:
        return f"{self.count} {self.name}"

    def __str__(self) -> str:
        return self.__repr__()

    @staticmethod
    def from_string(string) -> 'Material':
        count_string, name = string.split(" ")
        return Material(name.strip(), int(count_string))

class Reaction:

    inputs: List[Material]
    output: Material

    def __init__(self, inputs: List[Material], output: Material) -> None:
        self.inputs = inputs
        self.output = output

    def __repr__(self) -> str:
        output = ""
        input_strings = [str(material) for material in self.inputs]
        return ", ".join(input_strings) + " => " + str(self.output)

    def __str__(self) -> str:
        return self.__repr__()

    @staticmethod
    def from_input_line(line) -> 'Reaction':
        input_materials, output_material = line.split("=>")
        input_materials = input_materials.strip()
        output_material = output_material.strip()

        inputs = [Material.from_string(material) for material in input_materials.split(", ")]
        output = Material.from_string(output_material)

        return Reaction(inputs, output)


def create_material(material_to_create: str, count_required: int, spares: Dict[str, int], reactions: Dict[str, Reaction]) -> int:

    # Base case is ORE
    if material_to_create == "ORE":
        return count_required

    # Check if we have a stock first before we do anything else
    if material_to_create in spares:
        # Check if we have enough to fulfill the request outright
        if count_required <= spares[material_to_create]:
            spares[material_to_create] -= count_required
            return 0

        count_required -= spares[material_to_create]
        spares[material_to_create] = 0

    production_reaction = reactions[material_to_create]

    total_ore = 0
    recipe_iterations = math.ceil(count_required / production_reaction.output.count)
    created_material = recipe_iterations * production_reaction.output.count

    for input_material in production_reaction.inputs:
        input_material_count = input_material.count * recipe_iterations
        total_ore += create_material(input_material.name, input_material_count, spares, reactions)

    if created_material > count_required:
        spares[material_to_create] += created_material - count_required

    return total_ore


with open("year_2019/input_14.txt") as input_file:
        contents = input_file.read().strip()

all_reactions = {reaction.output.name: reaction for reaction in [Reaction.from_input_line(line) for line in contents.split("\n")]}

def part1():
    ore_per_unit_fuel = create_material("FUEL", 1, collections.defaultdict(lambda: 0), all_reactions)
    print("Part 1:", ore_per_unit_fuel)

def part2():
    ONE_TRILLION = 1_000_000_000_000

    fuel_count_high = ONE_TRILLION
    fuel_count_low = 1

    while True:
        fuel_count_mid = int((fuel_count_high + fuel_count_low) / 2)
        ore_count_mid = create_material("FUEL", fuel_count_mid, collections.defaultdict(lambda: 0), all_reactions)

        if ore_count_mid > ONE_TRILLION:
            fuel_count_high = fuel_count_mid
        elif ore_count_mid < ONE_TRILLION:
            fuel_count_low = fuel_count_mid

        if fuel_count_high - fuel_count_low <= 1:
            break

    print("Part 2:", fuel_count_low)

part1()
part2()