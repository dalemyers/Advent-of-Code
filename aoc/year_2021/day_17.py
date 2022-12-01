"""Day 17"""

import math
import re
from typing import List, Optional
from aoc.shared.maths import triangular
from aoc.shared.input import read_file_lines


def triangulars() -> List[int]:
    values = []
    v = 0
    dv = 0
    for _ in range(102):
        values.append(v)
        v += dv
        dv += 1

    return values[2:]


def run_probe(vx: int, vy: int, x1: int, x2: int, y1: int, y2: int):
    probe_x = 0
    probe_y = 0

    velocity_x = vx
    velocity_y = vy

    cx = math.ceil((x1 + x2) / 2)
    cy = math.ceil((y1 + y2) / 2)

    step = 0
    distances = [math.fabs(probe_y - cy)]

    while True:
        step += 1
        probe_x += velocity_x
        probe_y += velocity_y

        if velocity_x > 0:
            velocity_x -= 1
        elif velocity_x < 0:
            velocity_x += 1

        velocity_y -= 1

        distance = math.fabs(probe_y - cy)
        distances.append(distance)

        distances = distances[-3:]

        # If the distances away are increasing faster and faster, then we end
        # They can go further away, but the delta between them must decrease each time (indicating it's slowing down to change direction)
        if len(distances) == 3:
            if distances[-1] > distances[-2] > distances[-3]:
                if math.fabs(distances[-1] - distances[-2]) > math.fabs(
                    distances[-2] - distances[-3]
                ):
                    return False

        if x1 <= probe_x <= x2 and y1 <= probe_y <= y2:
            return True


def part1() -> int:
    """Part 1."""

    raw_string = read_file_lines("year_2021/input_17.txt")[0]

    match = re.match(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", raw_string)

    x1 = int(match.group(1))
    x2 = int(match.group(2))
    y1 = int(match.group(3))
    y2 = int(match.group(4))

    dy = int(math.fabs(y1 - y2))
    dx = int(math.fabs(x1 - x2))

    # Get the min and max x velocities
    min_xv = 0
    max_xv = 0
    distance_x = 0
    for i in range(1, x2):
        distance_x += i
        if min_xv == 0 and distance_x >= x1:
            min_xv = i
        if distance_x <= x2:
            max_xv = i
        else:
            break

    ys = []

    for xv in range(min_xv, 2 * x2):
        for yv in range(-200, 200):
            result = run_probe(xv, yv, x1, x2, y1, y2)
            if result:
                ys.append((xv, yv))

    ys.sort(key=lambda x: x[1])

    max_yv = ys[-1][1]

    max_y_height = triangular(max_yv)

    return max_y_height


def part2() -> int:
    """Part 2."""

    values = read_file_lines("year_2021/input_17.txt")[0]

    return 0


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
