import copy
from shared import get_positions, find_locations

with open("year_2015/input_19.txt") as f:
    contents = f.readlines()


def parse_molecule(string):
    output = []
    buffer = ""
    for character in string:
        if character.lower() == character:
            buffer += character
        else:
            output.append(buffer)
            buffer = character
    if buffer != "":
        output.append(buffer)
    return [m for m in output if len(m) > 0]


def replace_list(input_list, value, replacement, max_replacements=None):
    new_list = copy.deepcopy(input_list)
    if max_replacements is None:
        max_replacements = len(input_list)
    replacements = 0
    for index, original_value in enumerate(input_list):
        if original_value == value:
            new_list[index] = replacement
            replacements += 1
            if replacements >= max_replacements:
                return new_list

    return new_list


contents = [line.strip() for line in contents]
molecule_string = contents[-1]
contents = contents[:-2]

molecule = parse_molecule(molecule_string)

replacement_list = []
replacements = {}
constructions = {}
for line in contents:
    input_value, output_value = line.split(" => ")
    replacement_list.append((input_value, parse_molecule(output_value)))
    if replacements.get(input_value) is None:
        replacements[input_value] = []
    replacements[input_value].append(parse_molecule(output_value))
    replacements[input_value].sort(key=lambda x: len(x))
    constructions[output_value] = input_value


def part1():
    generated = []

    for key, values in replacements.items():
        for value in values:
            positions = get_positions(molecule, key)
            for position in positions:
                new_molecule = copy.deepcopy(molecule)
                new_molecule[position] = value
                new_molecule = [item for sublist in new_molecule for item in sublist]
                generated.append("".join(new_molecule))

    return len(set(generated))


def part2_ll():

    # Stupidly slow. I would guess this would take years to run at a minimum

    stack = [(0, ["e"])]

    solutions = []

    iterations = 0

    seen = set()

    while True:
        iterations += 1
        if iterations % 1000 == 0:
            print(iterations, len(stack), stack[len(stack) - 10000])
        if len(stack) == 0:
            break

        stack_count, last_value = stack.pop()

        if last_value == molecule:
            solutions.append(stack_count)
            continue

        if len(last_value) >= len(molecule):
            continue

        remaining_length = len(molecule) - len(last_value)

        for atom_index, atom in enumerate(last_value):
            for replacement in replacements.get(atom, []):
                if len(replacement) > remaining_length:
                    break
                new_attempt = last_value[:atom_index] + replacement + last_value[atom_index + 1 :]
                j = "".join(new_attempt)
                if j in seen:
                    continue
                seen.add(j)
                stack.append((stack_count + 1, new_attempt))

    return min(solutions)


def part2():

    molecule_str = "".join(molecule)

    stack = [(0, molecule_str)]

    reverses = [(k, v) for k, v in constructions.items()]
    reverses.sort(key=lambda x: len(x[0]))

    while True:
        if len(stack) == 0:
            break

        count, m = stack.pop()

        if m == "e":
            return count

        for compound, derivative in reverses:
            if compound not in m:
                continue

            locations = find_locations(m, compound)
            for location in locations:
                new_molecule = m[:location] + derivative + m[location + len(compound) :]
                stack.append((count + 1, new_molecule))

    return None


print("Part 1:", part1())
print("Part 2:", part2())
