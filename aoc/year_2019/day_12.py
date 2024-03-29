from functools import reduce
from math import gcd
import re
from typing import List, Optional, Tuple


class Moon:

    name: str
    x: int
    y: int
    z: int
    x_v: int
    y_v: int
    z_v: int

    def __init__(self, name: str, x: int, y: int, z: int) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.x_v = 0
        self.y_v = 0
        self.z_v = 0

    def update_position(self) -> None:
        self.x += self.x_v
        self.y += self.y_v
        self.z += self.z_v

    def potential_energy(self) -> int:
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kinetic_energy(self) -> int:
        return abs(self.x_v) + abs(self.y_v) + abs(self.z_v)

    def energy(self) -> int:
        return self.potential_energy() * self.kinetic_energy()

    def state_tuple(self) -> Tuple[int, int, int, int, int, int]:
        return (self.x, self.y, self.z, self.x_v, self.y_v, self.z_v)

    def __repr__(self) -> str:
        return f"name={self.name}, pos=<x={self.x}, y={self.y}, z={self.z}>, vel=<x={self.x_v}, y={self.y_v}, z={self.z_v}>"

    def __str__(self) -> str:
        return self.__repr__()


def compare_position(moon1, moon2) -> int:
    if moon2 > moon1:
        return 1
    elif moon2 == moon1:
        return 0
    else:
        return -1


def update_positions(all_moons: List[Moon]) -> None:
    for moon in all_moons:
        for other_moon in all_moons:
            if moon is other_moon:
                continue
            moon.x_v += compare_position(moon.x, other_moon.x)
            moon.y_v += compare_position(moon.y, other_moon.y)
            moon.z_v += compare_position(moon.z, other_moon.z)

    for moon in all_moons:
        moon.update_position()


def run_system(system_moons: List[Moon], steps: int) -> None:
    step = 1

    while True:
        update_positions(system_moons)

        print(f"After {step} steps:")
        for system_moon in system_moons:
            print(system_moon)
        print()

        if step >= steps:
            break

        step += 1

    total_energy = 0
    print(f"Energy after {step} steps:")
    for system_moon in system_moons:
        total_energy += system_moon.energy()
        print(system_moon.name, system_moon.energy())
    print("Total", total_energy)


def lcm(a, b):
    return int(a * b / gcd(a, b))


def lcms(*numbers):
    return reduce(lcm, numbers)


def find_period(system_moon: List[Moon]) -> Optional[int]:
    step = 1

    initial_x_state = [(moon.x, moon.x_v) for moon in system_moon]
    initial_y_state = [(moon.y, moon.y_v) for moon in system_moon]
    initial_z_state = [(moon.z, moon.z_v) for moon in system_moon]

    x_period = None
    y_period = None
    z_period = None

    while True:

        update_positions(system_moon)

        if not x_period:
            x_state = [(moon.x, moon.x_v) for moon in system_moon]
            if x_state == initial_x_state:
                x_period = step

        if not y_period:
            y_state = [(moon.y, moon.y_v) for moon in system_moon]
            if y_state == initial_y_state:
                y_period = step

        if not z_period:
            z_state = [(moon.z, moon.z_v) for moon in system_moon]
            if z_state == initial_z_state:
                z_period = step

        if x_period and y_period and z_period:
            break

        print(f"Step {step}")

        step += 1

    return lcms(x_period, y_period, z_period)


with open("year_2019/input_12.txt", encoding="utf-8") as input_file:
    contents = input_file.read().strip()

lines = contents.split("\n")
all_moons = []
names = ["Io", "Europa", "Ganymede", "Callisto"]

for line in lines:
    match = re.search(r"<x=(-?\d*), *y=(-?\d*), *z=(-?\d*)>", line)
    x, y, z = match.group(1), match.group(2), match.group(3)
    moon = Moon(names.pop(0), int(x), int(y), int(z))
    all_moons.append(moon)

# Part 1
run_system(all_moons, 1000)

# Part 2
print("Part 2:", find_period(all_moons))
