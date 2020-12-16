from collections import defaultdict
from shared import read_file_lines

contents = read_file_lines("year_2020/input_16.txt")

def get_info():
    fields = {}
    my_ticket = None
    other_tickets = []
    section = 1
    for line in contents:
        if line.strip() == "":
            section += 1
            continue

        if section == 1:
            field, ranges = line.split(": ")
            range1, range2 = ranges.split(" or ")
            r1 = (int(range1.split("-")[0]), int(range1.split("-")[1]))
            r2 = (int(range2.split("-")[0]), int(range2.split("-")[1]))
            fields[field] = (r1, r2)

        elif section == 2:
            if line.strip() == "your ticket:":
                continue
            my_ticket = list(map(int, line.split(",")))

        elif section == 3:
            if line.strip() == "nearby tickets:":
                continue
            other_tickets.append(list(map(int, line.split(","))))

    return fields, my_ticket, other_tickets


def in_ranges(value, ranges):
    for r in ranges:
        if r[0] <= value <= r[1]:
            return True
    return False


def get_invalid_values(ticket, fields):
    invalid_values = []
    for value in ticket:
        value_valid = False
        for field, ranges in fields.items():
            if in_ranges(value, ranges):
                value_valid = True
                break
        if not value_valid:
            invalid_values.append(value)
            break

    return invalid_values


def part1():
    fields, my_ticket, tickets = get_info()

    all_invalid_values = []

    for ticket in tickets:
        all_invalid_values += get_invalid_values(ticket, fields)

    return sum(all_invalid_values)

def part2():
    fields, my_ticket, tickets = get_info()

    valid_tickets = []

    # Filter out the totally invalid tickets
    for ticket in tickets:
        invalid_values = get_invalid_values(ticket, fields)
        if len(invalid_values) > 0:
            continue
        valid_tickets.append(ticket)

    # Find the possible colums for each field
    mappings = defaultdict(set)

    for i in range(len(ticket)):
        all_values = [ticket[i] for ticket in valid_tickets]
        for field, ranges in fields.items():
            invalid_value = False
            for value in all_values:
               if not in_ranges(value, ranges):
                   invalid_value = True
                   break

            if invalid_value:
                continue

            mappings[field].add(i)

    # Solve for the unique solution
    solution = []

    while len(mappings) > 0:
        for field, values in mappings.items():
            if len(values) == 1:
                solution.append((field, list(values)[0]))
                break
        del mappings[field]
        delete = solution[-1][1]
        for field, values in mappings.items():
            if delete in values:
                values.remove(delete)

    # Generate the value for the solution
    total = 1
    for name, value in solution:
        if name.startswith("departure"):
            total *= my_ticket[value]

    return total

print("Part 1:", part1())
print("Part 2:", part2())
