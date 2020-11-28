import itertools
import sys

def solve(iterations):
    input_value = "1113122113"

    for _ in range(iterations):
        output = ""
        i = 0
        c = input_value[i]
        buffer = input_value[i]

        while True:
            i += 1
            if i >= len(input_value):
                output += str(len(buffer)) + c
                break
            if input_value[i] == c:
                buffer += input_value[i]
                continue

            output += str(len(buffer)) + c
            c = input_value[i]
            buffer = input_value[i]

        input_value = output

    return len(output)

print("Part 1:", solve(40))
print("Part 1:", solve(50))
