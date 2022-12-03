from shared import read_file_lines, is_int
from operator import mul, add

contents = read_file_lines("year_2020/input_18.txt")


def evaluate_ltr(expression):
    output = expression[:]
    while "+" in output or "*" in output:
        if output[1] == "+":
            output = [int(output[0]) + int(output[2])] + output[3:]
        elif output[1] == "*":
            output = [int(output[0]) * int(output[2])] + output[3:]
    return output


def evaluate_operator(expression, operator, function):
    while operator in expression:
        location = expression.index(operator)
        expression = (
            expression[: location - 1]
            + [function(int(expression[location - 1]), int(expression[location + 1]))]
            + expression[location + 2 :]
        )
    return expression


def evaluate_precedence(expression, ltr_order=False):
    output = []
    i = -1
    while i < len(expression) - 1:
        i += 1

        term = expression[i]

        if term != "(":
            output.append(term)
            continue

        paren_count = 1
        for j in range(i + 1, len(expression)):
            j_term = expression[j]
            if j_term == "(":
                paren_count += 1
            elif j_term == ")":
                paren_count -= 1
            if paren_count == 0:
                output.append(evaluate_precedence(expression[i + 1 : j], ltr_order))
                i = j
                break

    # We should have no parentheses left

    if ltr_order:
        output = evaluate_ltr(output)
    else:
        output = evaluate_operator(output, "+", add)
        output = evaluate_operator(output, "*", mul)

    assert len(output) == 1
    return output[0]


def evaluate_string(line, ltr_order):
    line = line.replace("(", "( ").replace(")", " )")
    expression = line.split(" ")
    return evaluate_precedence(expression, ltr_order)


def part1():
    total = 0
    for line in contents:
        total += evaluate_string(line, True)
    return total


def part2():
    total = 0
    for line in contents:
        total += evaluate_string(line, False)
    return total


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
