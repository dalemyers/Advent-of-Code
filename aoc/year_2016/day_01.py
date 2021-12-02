import enum
import math

class Direction(enum.Enum):

    north = 'N'
    east = 'E'
    south = 'S'
    west = 'W'

    def right(self):
        if self == Direction.north:
            return Direction.east
        elif self == Direction.east:
            return Direction.south
        elif self == Direction.south:
            return Direction.west
        else:
            return Direction.north

    def left(self):
        if self == Direction.north:
            return Direction.west
        elif self == Direction.west:
            return Direction.south
        elif self == Direction.south:
            return Direction.east
        else:
            return Direction.north

with open("year_2016/input_01.txt") as f:
    contents = f.read()

commands = contents.strip().split(", ")
commands = [(command[0], int(command[1:])) for command in commands]

def part1():

    direction = Direction.north
    x = 0
    y = 0
    for command in commands:
        if command[0] == 'R':
            direction = direction.right()
        else:
            direction = direction.left()
        distance = int(command[1])
        if direction == Direction.north:
            y -= distance
        elif direction == Direction.south:
            y += distance
        elif direction == Direction.east:
            x += distance
        else:
            x -= distance

    return abs(x) + abs(y)


def part2():

    direction = Direction.north
    x = 0
    y = 0
    visited = set()
    for command in commands:
        if command[0] == 'R':
            direction = direction.right()
        else:
            direction = direction.left()
        distance = int(command[1])

        current_x = x
        current_y = y
        while distance > 0:
            if direction == Direction.north:
                current_y -= 1
            elif direction == Direction.south:
                current_y += 1
            elif direction == Direction.east:
                current_x += 1
            else:
                current_x -= 1
            new_location = (current_x, current_y)
            if new_location in visited:
                return abs(current_x) + abs(current_y)
            visited.add((current_x, current_y))
            distance -= 1
        x = current_x
        y = current_y


print("Part 1:", part1())
print("Part 2:", part2())
