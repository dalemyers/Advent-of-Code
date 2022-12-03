import re
from shared import read_file_lines, is_int

contents = read_file_lines("year_2020/input_19.txt")


class Disjunction(list):
    pass


def expand_disjunction(disjunction, rules):
    found_int = False
    output = []
    for component in disjunction:
        if is_int(component):
            replacement_rule = rules[int(component)]
            if type(replacement_rule) == str:
                output.append(replacement_rule)
            elif len(replacement_rule) == 1:
                output += expand_disjunction(replacement_rule[0], rules)
            else:
                disjunctions = []
                for subdisjunction in replacement_rule:
                    disjunctions.append(expand_disjunction(subdisjunction, rules))
                output.append(Disjunction(disjunctions))
        else:
            output.append(component)
    return output


def to_regex(rule, disjunction=False):
    output = []

    if type(rule) == str:
        return rule

    for component in rule:
        if type(component) == list:
            output += [to_regex(component)]
        elif type(component) == Disjunction:
            if all_letters(component):
                output += [to_regex(component, True)]
            else:
                output += ["(?:" + to_regex(component, True) + ")"]
        else:
            output += component
    if disjunction:
        return "|".join(output)
    else:
        return "".join(output)
    print()


def parse_input(replacements=None):
    rules = {}

    if replacements is None:
        replacements = {}

    for index, line in enumerate(contents):
        if line.strip() == "":
            break

        rule_id, content = line.split(": ")
        if rule_id in replacements:
            content = replacements[rule_id]

        disjunctions = content.split(" | ")
        parsed_disjunctions = []

        for disjunction in disjunctions:
            parsed_disjunction = []
            components = disjunction.split(" ")

            for component in components:
                if is_int(component):
                    parsed_disjunction.append(int(component))
                else:
                    parsed_disjunction.append(component[1:-1])

            parsed_disjunctions.append(Disjunction(parsed_disjunction))

        rules[int(rule_id)] = parsed_disjunctions

    messages = []
    for line in contents[index + 1 :]:
        messages.append(line)

    return rules, messages


def expand_rules(
    rules,
):

    p1_42 = expand_disjunction(rules[42][0], rules)
    p2_42 = expand_disjunction(rules[42][1], rules)
    p_42 = Disjunction([p1_42, p2_42])
    expanded_42 = to_regex(p_42, True)

    p1_31 = expand_disjunction(rules[31][0], rules)
    p2_31 = expand_disjunction(rules[31][1], rules)
    p_31 = Disjunction([p1_31, p2_31])
    expanded_31 = to_regex(p_31, True)

    if len(rules[8]) > 1 and 8 in rules[8][1]:
        rules[0] = expanded_42, expanded_31
        return

    rule_ids = sorted(rules.keys())
    for rule_id in rule_ids:
        disjunctions = rules[rule_id]
        expanded = []
        for disjunction in disjunctions:
            disjunction = expand_disjunction(disjunction, rules)
            expanded.append(disjunction)
        rules[rule_id] = expanded


def all_letters(clause):
    for character in clause:
        if character not in ["a", "b"]:
            return False
    return True


def part1():
    rules, messages = parse_input()
    expand_rules(rules)

    regex_pattern = "^" + to_regex(rules[0], True) + "$"

    match_count = 0
    for message in messages:
        if re.match(regex_pattern, message):
            match_count += 1

    return match_count


def part2():
    rules, messages = parse_input(
        {
            "8": "42 | 42 8",
            "11": "42 31 | 42 11 31",
        }
    )

    expand_rules(rules)

    r42, r31 = rules[0]

    match_count = 0
    for message in messages:
        found_match = False
        for n in range(1, 10):
            full_regex = f"^({r42})+?({r42}){{{n}}}({r31}){{{n}}}$"
            match = re.match(full_regex, message)
            if match:
                found_match = True
                break

        if found_match:
            match_count += 1
            continue

    return match_count


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
