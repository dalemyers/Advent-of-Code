"""Day 6"""

import enum

from aoc.shared import read_file_lines, print_raw_grid


class Direction(enum.Enum):

    up = "^"
    down = "v"
    left = "<"
    right = ">"

    def turn_right(self) -> "Direction":
        if self == Direction.up:
            return Direction.right
        if self == Direction.right:
            return Direction.down
        if self == Direction.down:
            return Direction.left
        if self == Direction.left:
            return Direction.up

    def delta(self) -> tuple[int, int]:
        if self == Direction.up:
            return 0, -1
        if self == Direction.down:
            return 0, 1
        if self == Direction.left:
            return -1, 0
        if self == Direction.right:
            return 1, 0


grid = [list(x) for x in read_file_lines("year_2024/input_06.txt")]


def find_guard() -> tuple[int, int]:
    for y, row in enumerate(grid):
        for x, character in enumerate(row):
            if character == "^":
                return x, y
    return None, None


def run_simulation(room: list[list[str]]) -> tuple[set[tuple[int, int]], list[tuple[int, int]], bool]:

    obstacles = []

    guard_x, guard_y = find_guard()

    visited = set()
    visited.add((guard_x, guard_y, Direction.up))

    direction = Direction.up
    while guard_y >= 0 and guard_y < len(room) and guard_x >= 0 and guard_x < len(room[0]):
        dx, dy = direction.delta()

        if guard_y + dy < 0 or guard_y + dy >= len(room) or guard_x + dx < 0 or guard_x + dx >= len(room[0]):
            break

        if room[guard_y + dy][guard_x + dx] in ["#", "O"]:
            obstacles.append((guard_x + dx, guard_y + dy))
            direction = direction.turn_right()
            continue
        else:
            guard_x += dx
            guard_y += dy

            if (guard_x, guard_y, direction) in visited:
                return visited, obstacles, True

            visited.add((guard_x, guard_y, direction))

    return visited, obstacles, False


def part1() -> int:
    """Part 1."""
    visited, _, _ = run_simulation(grid)
    visited_without_directions = set()
    for x, y, _ in visited:
        visited_without_directions.add((x, y))

    return len(visited_without_directions)


def part2() -> int:
    """Part 2."""
    visited, obstacles, _ = run_simulation(grid)
    visited_without_directions = set()
    for x, y, _ in visited:
        visited_without_directions.add((x, y))

    valid_obstacle_locations = set()

    # This is the brute force approach. I tried a different one below where I
    # calculated the next obstacle positions based on the current ones. It
    # should be have been significantly faster, but I couldn't get it to work.
    for y in range(len(grid)):
        print(y, len(grid))
        for x in range(len(grid[0])):
            if (x, y) in visited_without_directions:
                prev_char = grid[y][x]
                if prev_char == "^":
                    continue
                grid[y][x] = "O"
                _, _, was_loop = run_simulation(grid)
                if was_loop:
                    valid_obstacle_locations.add((x, y))
                grid[y][x] = prev_char

    return len(valid_obstacle_locations)

    valid_obstacle_locations = set()

    for o_a, o_b, o_c in zip(obstacles, obstacles[1:], obstacles[2:]):
        next_x = o_a[0] - 1
        next_y = o_c[1] - 1

        next_options = [
            (o_a[0] + 1, o_c[1] + 1),
            (o_a[0] - 1, o_c[1] - 1),
            (o_a[0] + 1, o_c[1] - 1),
            (o_a[0] - 1, o_c[1] + 1),
            (o_a[0], o_b[1]),
            (o_c[0], o_b[1]),
            (o_b[0], o_a[1]),
            (o_b[0], o_c[1]),
        ]

        for next_x, next_y in next_options:
            if (next_x, next_y) not in visited_without_directions:
                continue

            grid[next_y][next_x] = "O"

            _, _, was_loop = run_simulation(grid)

            if was_loop:
                valid_obstacle_locations.add((next_x, next_y))
                # print_raw_grid(grid)
                # print()

            grid[next_y][next_x] = "."

            # print(next_x, next_y)

    return len(valid_obstacle_locations)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
