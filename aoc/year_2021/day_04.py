"""Day 4"""

from typing import List, Tuple
from aoc.shared import read_file_lines


class Cell:
    """Cell on a bingo board."""

    marked: bool

    def __init__(self, value: int) -> None:
        self.value = value
        self.marked = False

    def mark(self) -> None:
        self.marked = True

    def __str__(self) -> str:
        if self.marked:
            return f"({self.value})"
        else:
            return f" {self.value} "

    def __repr__(self) -> str:
        return str(self)


class Board:
    def __init__(self, cells: List[List[Cell]]) -> None:
        self.cells = cells

    def mark(self, value: int) -> None:
        for row in self.cells:
            for cell in row:
                if cell.value == value:
                    cell.mark()
                    return

    def has_win(self) -> bool:
        for row in self.cells:
            if all([cell.marked for cell in row]):
                return True

        for row in list(map(list, zip(*self.cells))):
            if all([cell.marked for cell in row]):
                return True

    @staticmethod
    def from_values(values: List[str]) -> "Board":
        rows = []
        for row in values:
            numbers = [Cell(int(x)) for x in row.split(" ") if len(x.strip()) > 0]
            rows.append(numbers)
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
        for cell in row:
            if cell.marked:
                continue
            total += cell.value

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

        if len(boards) == 1 and boards[0].has_win():
            winning_call = call
            break

        # Make sure we don't delete one and mess up the next index
        winning_boards.sort(reverse=True)

        for winning_board in winning_boards:
            del boards[winning_board]

        winning_boards = []

    total = 0
    for row in boards[0].cells:
        for cell in row:
            if cell.marked:
                continue
            total += cell.value

    return total * winning_call


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
