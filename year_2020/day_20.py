import copy
from collections import defaultdict
from itertools import permutations
import enum
import math
from shared import read_file_lines, print_raw_grid

contents = read_file_lines("year_2020/input_20.txt")

class Flip(enum.Enum):
    horizontal = "horizontal"
    vertical = "vertical"

class Rotation(enum.Enum):
    one = 1
    two = 2
    three = 3


def get_tiles():
    tiles = {}
    buffer = []
    tile_id = 0
    for line in contents:
        if line.startswith("Tile "):
            tile_id = int(line[5:-1])
            continue

        if line.strip() == "":
            tiles[tile_id] = buffer
            buffer = []
            continue

        buffer.append([c for c in line])

    tiles[tile_id] = buffer
    return tiles


def get_borders(tiles):
    borders = {}
    for tile_id, tile in tiles.items():
        tile_borders = [
            (tile[0], []),
            (tile[-1], [Flip.vertical]),
            ([r[0] for r in tile], [Rotation.three, Flip.vertical]),
            ([r[-1] for r in tile], [Rotation.one]),
            (tile[0][::-1], [Flip.horizontal]),
            (tile[-1][::-1], [Flip.horizontal, Flip.vertical]),
            ([r[0] for r in tile][::-1], [Rotation.three]),
            ([r[-1] for r in tile][::-1], [Rotation.one, Flip.horizontal]),
        ]
        borders[tile_id] = tile_borders

    return borders

def opposite_index(index):
    return {
        0: 1,
        1: 0,
        2: 3,
        3: 2,
        4: 5,
        5: 4,
        6: 7,
        7: 6,
    }[index]


def bottom_index_for_left_border(border):
    return {
        0: 3,
        1: 7,
        2: 1,
        3: 5,
        4: 2,
        5: 6,
        6: 0,
        7: 4,
    }[border]


def left_index_for_bottom_border(border):
    return {
        0: 6,
        1: 2,
        2: 4,
        3: 0,
        4: 7,
        5: 3,
        6: 5,
        7: 1,
    }[border]


def top_index_for_left_border(border):
    return {
        0: 2,
        1: 6,
        2: 0,
        3: 4,
        4: 3,
        5: 7,
        6: 1,
        7: 5,
    }[border]



def left_index_for_top_border(border):
    return {
        0: 2,
        1: 6,
        2: 0,
        3: 4,
        4: 3,
        5: 7,
        6: 1,
        7: 5,
    }[border]



def get_next_in_row(current, length, pairs):
    if len(current) == length:
        yield current

    previous_id, previous_index = current[-1]
    valid_pairs = pairs[(previous_id, opposite_index(previous_index))]
    used = {c[0] for c in current}

    for t2_id, i2 in valid_pairs:
        if t2_id in used:
            continue
        yield from get_next_in_row(current + [(t2_id, i2)], length, pairs)


def get_rows(borders, pairs, length):
    for t1_id, t1 in borders.items():
        for i in range(len(t1)):
            row = [(t1_id, i)]
            yield from get_next_in_row(row, length, pairs)



def build_pairs(borders):
    pairs = defaultdict(set)

    for t1_id, t1 in borders.items():
        for t2_id, t2 in borders.items():
            if t1_id == t2_id:
                continue
            for i1, (b1, o1) in enumerate(t1):
                for i2, (b2, o2) in enumerate(t2):
                    if b1 == b2:
                        pairs[(t1_id, i1)].add((t2_id, i2))
                        pairs[(t2_id, i2)].add((t1_id, i1))

    return pairs


def perform_flip(operation, tile):
    if operation == Flip.horizontal:
        output = []
        for row in tile:
            output.append(row[::-1])
        return output

    return tile[::-1]


def perform_rotation(operation, tile):
    rotated = list(zip(*tile[::-1]))
    if operation == Rotation.one:
        return rotated
    rotated = list(zip(*rotated[::-1]))
    if operation == Rotation.two:
        return rotated
    rotated = list(zip(*rotated[::-1]))
    return rotated



def perform_operations(tile, operations):
    for operation in operations:
        if isinstance(operation, Flip):
            tile = perform_flip(operation, tile)
        else:
            tile = perform_rotation(operation, tile)

    return tile


def get_next_row(previous_row, borders, pairs, used_ids):

    output = []
    for upper_tile_id, upper_tile_border in previous_row:
        upper_tile_bottom_index = bottom_index_for_left_border(upper_tile_border)
        matches = list(pairs[(upper_tile_id, upper_tile_bottom_index)])

        if len(matches) == 0:
            output = []
            break

        elif len(matches) == 1:
            current_tile_id, current_tile_left_index = matches[0][0], left_index_for_top_border(matches[0][1])

            if current_tile_id in used_ids:
                output = []
                break

            if len(output) >= 1:
                previous_tile_id, previous_tile_left_border_index = output[-1]
                previous_tile_right_border_index = opposite_index(previous_tile_left_border_index)
                previous_right_border = borders[previous_tile_id][previous_tile_right_border_index]
                current_left_border = borders[current_tile_id][current_tile_left_index]
                if previous_right_border[0] != current_left_border[0]:
                    output = []
                    break

            output.append((current_tile_id, current_tile_left_index))

        else:
            print()

    return output


def get_unique_rows(borders, pairs, dimension):

    for row in get_rows(borders, pairs, dimension):
        if row[0][0] == 1951 and row[1][0] == 2311 and row[2][0] == 3079:
            if row[0][1] == 6 and row[1][1] == 6 and row[2][1] == 2:
                _ = 1
        next_rows = [row]
        used_ids = set([tile[0] for tile in row])
        while len(next_rows) < dimension:
            next_row = get_next_row(next_rows[-1], borders, pairs, used_ids)
            used_ids |= set([tile[0] for tile in next_row])
            if len(next_row) == 0:
                break
            next_rows.append(next_row)

        if len(next_rows) == dimension:
            yield next_rows



def part1_solutions():
    tiles = get_tiles()
    borders = get_borders(tiles)
    dimension = int(math.sqrt(len(borders)))
    pairs = build_pairs(borders)

    for rows in get_unique_rows(borders, pairs, dimension):
        #if rows[0][0][0] == 1951 and rows[0][1][0] == 2311 and rows[0][2][0] == 3079:
        #    if rows[1][0][0] == 2729 and rows[1][1][0] == 1427 and rows[1][2][0] == 2473:
        #        if rows[2][0][0] == 2971 and rows[2][1][0] == 1489 and rows[2][2][0] == 1171:
        #            _ = 1
        #            if rows[1][0][1] == 6 and rows[1][1][1] == 6 and rows[1][2][1] == 2:
        #                if rows[0][0][1] == 6 and rows[0][1][1] == 6 and rows[0][2][1] == 5:
        #                    if rows[2][0][1] == 6 and rows[2][1][1] == 6 and rows[2][2][1] == 3:
        #                        _ = 1

        yield rows
        

def part1():
    for rows in part1_solutions():
        tl = rows[0][0][0]
        tr = rows[0][-1][0]
        bl = rows[-1][0][0]
        br = rows[-1][-1][0]
        total = tl * tr * bl * br
        return total



def part2():
    pass

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
