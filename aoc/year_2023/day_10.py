"""Day 10"""

from aoc.shared import read_file_lines

lines = read_file_lines("year_2023/input_10.txt")


def get_start() -> tuple[int, int]:
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "S":
                return x, y


def get_next_for_start(sx, sy):
    output = []
    if lines[sy - 1][sx] in "|7F":
        return (0, -1)
    if lines[sy][sx - 1] in "-LF":
        return (-1, 0)
    if lines[sy][sx + 1] in "-J7":
        return (1, 0)
    if lines[sy + 1][sx] in "|LJ":
        return (0, 1)

    return output


def get_next(x, y, dx, dy):
    c = lines[y][x]

    if c == "-":
        if dx > 0:
            return 1, 0
        if dx < 0:
            return -1, 0
        raise ValueError()

    if c == "7":
        if dx > 0:
            return 0, 1
        if dy < 0:
            return -1, 0
        raise ValueError()

    if c == "|":
        if dy > 0:
            return 0, 1
        if dy < 0:
            return 0, -1
        raise ValueError()

    if c == "J":
        if dy > 0:
            return -1, 0
        if dx > 0:
            return 0, -1
        raise ValueError()

    if c == "L":
        if dy > 0:
            return 1, 0
        if dx < 0:
            return 0, -1
        raise ValueError()

    if c == "F":
        if dy < 0:
            return 1, 0
        if dx < 0:
            return 0, 1
        raise ValueError()

    raise ValueError()


def get_loop() -> list[tuple[int, int]]:
    steps = []
    x, y = get_start()
    steps.append((x, y))
    dx, dy = get_next_for_start(x, y)
    x, y = x + dx, y + dy
    steps.append((x, y))

    while True:
        dx, dy = get_next(x, y, dx, dy)
        x, y = x + dx, y + dy
        if lines[y][x] == "S":
            break
        steps.append((x, y))
    return steps


def part1() -> int:
    """Part 1."""
    steps = get_loop()
    return int(len(steps) / 2)


def part2() -> int:
    """Part 2."""
    steps = get_loop()
    board = [line[:] for line in lines]
    for y in range(0, len(board)):
        for x in range(0, len(board[y])):
            if (x, y) not in steps:
                board[y] = board[y][:x] + " " + board[y][x + 1 :]

    for line in board:
        print(line)
    return int(len(steps) / 2)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
