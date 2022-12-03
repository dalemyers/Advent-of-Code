import re
import operator as op
from shared import is_int

with open("year_2015/input_07.txt") as f:
    contents = f.read()

gate_identifier = {
    "AND": op.and_,
    "OR": op.or_,
    "LSHIFT": op.lshift,
    "RSHIFT": op.rshift,
}

data = {}


def resolve(b_override=None):
    global data
    data = {}

    for line in contents.splitlines():
        input_text, output = line.split(" -> ")
        components = input_text.split(" ")

        components = [
            int(component) if is_int(component) else component for component in components
        ]

        if len(components) == 1:
            if is_int(components[0]):
                data[output] = (int(components[0]), None, None)
            else:
                data[output] = (components[0], None, None)
            continue

        if len(components) == 2:
            data[output] = (lambda x, y: x ^ 65535, components[1], None)
        elif len(components) == 3:
            data[output] = (
                gate_identifier[components[1]],
                components[0],
                components[2],
            )

    if b_override is not None:
        data["b"] = (b_override, None, None)

    while True:

        identifier_found = False

        for key in data.keys():
            operator, input1, input2 = data[key]

            if is_int(operator):
                continue

            if isinstance(operator, str):
                check = data[operator]
                if is_int(check[0]):
                    operator = check[0]
                    data[key] = (operator, None, None)
                    continue
                else:
                    continue
            else:
                if is_int(input1) and (input2 is None or is_int(input2)):
                    data[key] = (operator(input1, input2) & 65535, None, None)
                    continue

            if not is_int(input1):
                identifier_found = True
                check = data[input1]
                if is_int(check[0]):
                    input1 = check[0]
                    data[key] = (operator, input1, input2)

            if input2 and not is_int(input2):
                identifier_found = True
                check = data[input2]
                if is_int(check[0]):
                    input2 = check[0]
                    data[key] = (operator, input1, input2)

        if not identifier_found:
            break


resolve()
print("Part 1:", data["a"][0])
resolve(data["a"][0])
print("Part 2:", data["a"][0])
