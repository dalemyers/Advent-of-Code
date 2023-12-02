"""Day 2"""

from aoc.shared import read_file_lines

lines = read_file_lines("year_2023/input_02.txt")

Handful = dict[str, int]
Game = tuple[int, list[Handful]]


def parse_handful(handful: str) -> Handful:
    cubes_str = handful.strip().split(",")
    output = {}

    for cube_str in cubes_str:
        cube_str = cube_str.strip()
        count_str, color = cube_str.split(" ")
        output[color.strip()] = int(count_str)

    return output


def parse_game(line: str) -> Game:
    identifier_str, contents_str = line.split(":")
    identifier = int(identifier_str.strip().replace("Game ", ""))
    handfuls_str = contents_str.split(";")
    handfuls = [parse_handful(handful) for handful in handfuls_str]

    return (identifier, handfuls)


def parse_games() -> list[Game]:
    output = []
    for line in lines:
        output.append(parse_game(line))
    return output


def part1() -> int:
    """Part 1."""
    load = {"red": 12, "green": 13, "blue": 14}
    games = parse_games()
    ids = []

    for game_id, handfuls in games:
        impossible = False
        for handful in handfuls:
            for colour, count in handful.items():
                if colour not in load:
                    impossible = True
                    break

                if count > load[colour]:
                    impossible = True
                    break

            if impossible:
                break

        if impossible:
            continue

        ids.append(game_id)

    return sum(ids)


def part2() -> int:
    """Part 2."""

    games = parse_games()
    powers = []

    for _, handfuls in games:
        load = {}
        for handful in handfuls:
            for colour, count in handful.items():
                if colour not in load:
                    load[colour] = count
                    continue

                load[colour] = max(load[colour], count)

        power = 1
        for value in load.values():
            power *= value

        powers.append(power)

    return sum(powers)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
