import copy
import enum
from shared import read_file_lines

contents = read_file_lines("year_2020/input_12.txt")

class Direction(enum.Enum):
    north = "N"
    east = "E"
    south = "S"
    west = "W"

    def turn(self, angle):
        angle = int(angle % 360)
        angle = int(angle / 90)
        lookup = {
            Direction.north: [Direction.north, Direction.east, Direction.south, Direction.west],
            Direction.east: [Direction.east, Direction.south, Direction.west, Direction.north],
            Direction.south: [Direction.south, Direction.west, Direction.north, Direction.east],
            Direction.west: [Direction.west, Direction.north, Direction.east, Direction.south],
        }
        return lookup[self][angle]

    def delta(self, distance):
        if self == Direction.north:
            return (0, -distance)
        elif self == Direction.south:
            return (0, distance)
        elif self == Direction.east:
            return (distance, 0)
        elif self == Direction.west:
            return (-distance, 0)


def part1():
    direction = Direction.east
    x, y = 0, 0
    for line in contents:
        letter = line[0]
        magnitude = int(line[1:])
        if letter == "F":
            dx, dy = direction.delta(magnitude)
            x += dx
            y += dy
        elif letter == "R":
            direction = direction.turn(magnitude)
        elif letter == "L":
            direction = direction.turn(-magnitude)
        elif letter == "N":
            y -= magnitude
        elif letter == "E":
            x += magnitude
        elif letter == "S":
            y += magnitude
        elif letter == "W":
            x -= magnitude

    return abs(x) + abs(y)

def part2():
    direction = Direction.east
    wx, wy = 10, -1
    x, y = 0, 0
    for line in contents:
        letter = line[0]
        magnitude = int(line[1:])
        if letter == "F":
            for _ in range(magnitude):
                x += wx
                y += wy
        elif letter in ["R", "L"]:
            rotations = int((magnitude % 360) / 90)
            for _ in range(rotations):
                if letter == "R":
                    wx, wy = -wy, wx
                else:
                    wx, wy = wy, -wx
        elif letter == "N":
            wy -= magnitude
        elif letter == "E":
            wx += magnitude
        elif letter == "S":
            wy += magnitude
        elif letter == "W":
            wx -= magnitude

    return abs(x) + abs(y)



print("Part 1:", part1())
print("Part 2:", part2())
