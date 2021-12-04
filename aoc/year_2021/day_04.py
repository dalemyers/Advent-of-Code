"""Day 4"""

from typing import List, Optional, Tuple
from aoc.shared import read_file_lines, transpose


class Board:
    def __init__(self, cells: List[List[Optional[int]]]) -> None:
        self.cells = cells

    def mark(self, value: int) -> None:
        for y, row in enumerate(self.cells):
            for x, v in enumerate(row):
                if value == v:
                    self.cells[y][x] = None
                    return

    def has_win(self) -> bool:
        for row in self.cells + transpose(self.cells):
            if all(cell is None for cell in row):
                return True
        return False

    @staticmethod
    def from_values(values: List[str]) -> "Board":
        rows = []
        for row in values:
            rows.append([int(x) for x in row.split(" ") if len(x.strip()) > 0])
        return Board(rows)


def load_boards() -> Tuple[List[int], Board]:
    lines = read_file_lines("year_2021/input_04.txt")

    calls = [int(x) for x in lines[0].split(",")]
    lines = lines[2:]

    boards = []
    raw_board = []

    while len(lines) > 0:
        line = lines.pop(0)
        if line != "":
            raw_board.append(line)

        if line == "" or len(lines) == 0:
            boards.append(Board.from_values(raw_board))
            raw_board = []

    return calls, boards


def part1() -> int:
    """Part 1."""

    calls, boards = load_boards()

    winning_board = None
    winning_call = None

    for call in calls:
        for board in boards:
            board.mark(call)
            if board.has_win():
                winning_board = board
                winning_call = call
                break

        if winning_board:
            break

    total = 0
    for row in winning_board.cells:
        total += sum(v for v in row if v is not None)

    return total * winning_call


def part2() -> int:
    """Part 2."""

    calls, boards = load_boards()

    winning_boards = []
    winning_call = None

    for call in calls:
        for index, board in enumerate(boards):
            board.mark(call)
            if board.has_win():
                winning_boards.append(index)

        if len(boards) == 1 and len(winning_boards):
            winning_call = call
            break

        # Make sure we don't delete one and mess up the next index
        winning_boards.sort(reverse=True)

        for winning_board in winning_boards:
            del boards[winning_board]

        winning_boards = []

    total = 0
    for row in boards[0].cells:
        total += sum(v for v in row if v is not None)

    return total * winning_call


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
