from shared import read_file_lines

contents = read_file_lines("year_2020/input_05.txt")

def handle_boarding_pass(boarding_pass):
    lower = 0
    upper = 127
    left = 0
    right = 7

    for character in boarding_pass[:7]:
        if character == "F":
            upper = int((lower + upper + 1) / 2) - 1
        else:
            lower = int((lower + upper + 1) / 2) 

    for character in boarding_pass[7:]:
        if character == "L":
            right = int((left + right + 1) / 2) - 1
        else:
            left = int((left + right + 1) / 2) 

    row = lower
    column = left
    seat_id = (row * 8) + column

    return (row, column, seat_id)


def part1():
    seat_ids = []
    for boarding_pass in contents:
        _, _, seat_id = handle_boarding_pass(boarding_pass)
        seat_ids.append(seat_id)

    return max(seat_ids)


def part2():
    seats = []
    for boarding_pass in contents:
        row, column, _ = handle_boarding_pass(boarding_pass)
        seats.append((row, column))

    seats.sort()

    previous_row = None
    previous_column = -1

    for row, column in seats:
        if previous_row is None:
            previous_row = row
            previous_column = column
            continue

        if row != previous_row:
            previous_column = -1
            previous_row = row

        if column != previous_column + 1:
            return (row * 8) + (column - 1)
        else:
            previous_column = column

    print()


print("Part 1:", part1())
print("Part 2:", part2())
