import copy
import enum
from shared import read_file_lines

contents = read_file_lines("year_2020/input_11.txt")

class State(enum.Enum):
    floor = "."
    empty = "L"
    occupied = "#"


def get_state():
    output = []
    for line in read_file_lines("year_2020/input_11.txt"):
        row = []
        for character in line:
            row.append(State(character))
        output.append(row)
    return output


def get_surrounding_count(grid, x, y):
    count = 0
    for y_index in range(y - 1, y + 2):
        if y_index < 0 or y_index >= len(grid):
            continue
        for x_index in range(x - 1, x + 2):
            if x_index < 0 or x_index >= len(grid[0]):
                continue

            if x == x_index and y == y_index:
                continue

            if grid[y_index][x_index] == State.occupied:
                count += 1
    return count


def print_grid(grid):
    return
    for row in grid:
        print("".join([s.value for s in row]))
    print()

def get_occupied_count(grid):
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == State.occupied:
                count += 1
    return count

def _iterate_sequence(sequence, start_index):
    index = start_index
    count = 0
    while True:
        index += 1
        if index >= len(sequence):
            break
        if sequence[index] != State.floor:
            if sequence[index] == State.occupied:
                count += 1
            break
    
    index = start_index
    while True:
        index -= 1
        if index < 0:
            break
        if sequence[index] != State.floor:
            if sequence[index] == State.occupied:
                count += 1
            break

    return count

def _get_diagonal1(grid, x, y):
    start_location = 0

    output = [grid[y][x]]
    x_index = x
    y_index = y
    while True:
        x_index += 1
        y_index += 1
        if x_index >= len(grid[0]) or y_index >= len(grid):
            break
        output.append(grid[y_index][x_index])

    x_index = x
    y_index = y
    while True:
        x_index -= 1
        y_index -= 1
        if x_index < 0 or y_index < 0:
            break
        output.insert(0, grid[y_index][x_index])
        start_location += 1

    return output, start_location


def _get_diagonal2(grid, x, y):
    start_location = 0

    output = [grid[y][x]]
    x_index = x
    y_index = y
    while True:
        x_index += 1
        y_index -= 1
        if x_index >= len(grid[0]) or y_index < 0:
            break
        output.append(grid[y_index][x_index])

    x_index = x
    y_index = y
    while True:
        x_index -= 1
        y_index += 1
        if x_index < 0 or y_index >= len(grid):
            break
        output.insert(0, grid[y_index][x_index])
        start_location += 1

    return output, start_location


def get_visible(grid, x, y):
    count = 0
    # Row
    row = grid[y]
    count += _iterate_sequence(row, x)

    # Column
    column = [row[x] for row in grid]
    count += _iterate_sequence(column, y)

    # Diagonal 1
    d1, index1 = _get_diagonal1(grid, x, y)
    count += _iterate_sequence(d1, index1)

    # Diagonal 2
    d2, index2 = _get_diagonal2(grid, x, y)
    count += _iterate_sequence(d2, index2)

    return count


def part1():
    state = get_state()
    print_grid(state)
    while True:
        original = copy.deepcopy(state)
        for y in range(len(state)):
            for x in range(len(state[0])):
                if original[y][x] == State.floor:
                    continue
                count = get_surrounding_count(original, x, y)
                if original[y][x] == State.occupied:
                    if count >= 4:
                        state[y][x] = State.empty
                elif original[y][x] == State.empty:
                    if count == 0:
                        state[y][x] = State.occupied
        print_grid(state)
        if original == state:
            break

    return get_occupied_count(state)

def part2():
    state = get_state()
    print_grid(state)
    while True:
        original = copy.deepcopy(state)
        for y in range(len(state)):
            for x in range(len(state[0])):
                if original[y][x] == State.floor:
                    continue
                count = get_visible(original, x, y)
                if original[y][x] == State.occupied:
                    if count >= 5:
                        state[y][x] = State.empty
                elif original[y][x] == State.empty:
                    if count == 0:
                        state[y][x] = State.occupied
        print_grid(state)
        if original == state:
            break

    return get_occupied_count(state)

print("Part 1:", part1())
print("Part 2:", part2())
