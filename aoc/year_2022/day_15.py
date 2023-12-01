"""Day 15"""

from collections import defaultdict
import re
import sys
from typing import Dict, List, Set, Tuple
from aoc.shared import read_file_lines, Point

lines = read_file_lines("year_2022/input_15.txt")

DEBUG = False


class Sensor:
    def __init__(self, location: Point, beacon: Point) -> None:
        self.location = location
        self.beacon = beacon

    def beacon_distance(self) -> int:
        return self.distance_to(self.beacon.x, self.beacon.y)

    def distance_to(self, x: int, y: int) -> int:
        return self.location.manhattan_distance(x, y)


class Beacon:
    def __init__(self, location: Point, sensors: List[Sensor]) -> None:
        self.location = location
        self.sensors = sensors

    def distance_to(self, x: int, y: int) -> int:
        return self.location.manhattan_distance(x, y)


def load() -> Tuple[List[Point], Set[Point]]:

    pattern = (
        r"Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)"
    )
    sensors = []
    beacons = set()
    for line in lines:
        match = re.match(pattern, line)
        sx = int(match.group(1))
        sy = int(match.group(2))
        bx = int(match.group(3))
        by = int(match.group(4))
        beacon = Point(bx, by)
        sensors.append(Sensor(Point(sx, sy), beacon))
        beacons.add(beacon)

    return sensors, beacons


def grid_size(grid: Dict[Point, str]):
    min_x = sys.maxsize
    max_x = -sys.maxsize
    min_y = sys.maxsize
    max_y = -sys.maxsize

    keys = list(grid.keys())

    for x, y in keys:
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    return min_x, max_x, min_y, max_y


def print_sparse_grid(grid: Dict[Point, str]) -> None:

    if not DEBUG:
        return

    min_x, max_x, min_y, max_y = grid_size(grid)

    for y in range(min_y, max_y + 1):
        if y < 0:
            print(str(y), end="", sep="")
        elif y < 10:
            print("0" + str(y), sep="", end="")
        else:
            print(y, sep="", end="")

        print(" ", end="", sep="")

        for x in range(min_x, max_x + 1):
            print(grid.get(Point(x, y), "."), sep="", end="")
        print()

    print()


def part1_v1() -> int:
    """Part 1."""

    sensors, beacons = load()

    grid = {}

    for sensor in sensors:
        grid[sensor.location] = "S"

    for beacon in beacons:
        grid[beacon] = "B"

    min_x, max_x, _, _ = grid_size(grid)

    print_sparse_grid(grid)

    for index, sensor in enumerate(sensors):
        print(index, len(sensors))
        distance = sensor.beacon_distance()
        for x in range(sensor.location.x - distance, sensor.location.x + distance + 1):
            for y in range(
                sensor.location.y - distance, sensor.location.y + distance + 1
            ):
                point_distance = sensor.distance_to(x, y)
                if point_distance > distance:
                    continue
                if grid.get(Point(x, y), ".") == ".":
                    grid[Point(x, y)] = "#"
        print_sparse_grid(grid)

    output = ""
    for x in range(min_x, max_x + 1):
        output += grid.get(Point(x, 10), ".")

    return output.count("#")


def part1_v2() -> int:
    """Part 1."""

    y_value = 2000000
    sensors, beacon_location = load()

    beacons = defaultdict(list)

    for sensor in sensors:
        beacons[sensor.beacon].append(sensor)

    grid = {}

    for sensor in sensors:
        grid[(sensor.location.x, sensor.location.y)] = "S"

    for beacon in beacons:
        grid[(beacon.x, beacon.y)] = "B"

    min_x, max_x, min_y, max_y = grid_size(grid)
    cannot_be_sensor = 0

    for x in range(min_x, max_x + 1):
        if x % 1000 == 0:
            print(100 * (x - min_x) / (max_x - min_x))

        if grid.get((x, y_value)) is not None:
            continue

        distances = []
        for sensor in sensors:
            distance = 0
            if sensor.location.x > x:
                distance += sensor.location.x - x
            else:
                distance += x - sensor.location.x

            if sensor.location.y > y_value:
                distance += sensor.location.y - y_value
            else:
                distance += y_value - sensor.location.y

            if distance < sensor.beacon_distance():
                continue

            distances.append(distance)

        distances.sort()

        if len(distances) < 2:
            continue

        if distances[0] != distances[1]:
            cannot_be_sensor += 1

    return cannot_be_sensor


def part1() -> int:
    """Part 1."""
    y_value = 2000000
    sensors, _ = load()
    grid = {}

    for sensor in sensors:
        grid[(sensor.location.x, sensor.location.y)] = "S"
        grid[(sensor.beacon.x, sensor.beacon.y)] = "B"

    min_x, max_x, _, _ = grid_size(grid)
    cannot_be_sensor = 0

    in_range = []

    for sensor in sensors:
        distance_to_y = 0
        if sensor.location.y > y_value:
            distance_to_y = sensor.location.y - y_value
        else:
            distance_to_y = y_value - sensor.location.y

        if distance_to_y > sensor.beacon_distance():
            continue

        in_range.append((sensor, distance_to_y))

    covered = {}

    for sensor, y_distance in in_range:
        sensor_range = sensor.beacon_distance()
        delta = sensor_range - y_distance

        left = sensor.location.x - delta
        right = sensor.location.x + delta

        for x in range(left, right + 1):
            covered[x] = True

    for x in range(min_x, max_x + 1):
        if grid.get((x, y_value)) is not None:
            continue

        if covered.get(x, False) is True:
            cannot_be_sensor += 1

    return cannot_be_sensor


# 3869892
# 3869895
def part2() -> int:
    """Part 2."""

    return simulate(floor=True)


if __name__ == "__main__":
    print("Part 1:", part1())
    # print("Part 2:", part2())
