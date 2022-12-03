import itertools
import re


with open("year_2015/input_13.txt") as f:
    input_data = f.read()

# Mallory would gain 22 happiness units by sitting next to Eric.

pattern = re.compile(r"(.*) would (.*) (\d*) happiness units by sitting next to (.*)\.")

data = {}

for line in input_data.splitlines():
    match = pattern.match(line)
    assert match is not None
    person1 = match.group(1)
    result = match.group(2)
    delta = int(match.group(3))
    if result == "lose":
        delta = -delta
    person2 = match.group(4)
    print(person1, delta, person2)
    if data.get(person1) is None:
        data[person1] = {}
    data[person1][person2] = delta


def part1():
    people = list(data.keys())

    max_happiness = 0
    permutations = list(itertools.permutations(people))
    for index, permutation in enumerate(permutations):
        print(index, "/", len(permutations))
        permutation = list(permutation)
        p_total = 0
        for p1, p2 in zip(permutation, permutation[1:] + [permutation[0]]):
            p_total += data[p1][p2]
            p_total += data[p2][p1]

        if p_total > max_happiness:
            max_happiness = p_total

    return max_happiness


def part2():
    people = list(data.keys()) + ["me"]

    max_happiness = 0
    permutations = list(itertools.permutations(people))
    for index, permutation in enumerate(permutations):
        print(index, "/", len(permutations))
        permutation = list(permutation)
        p_total = 0
        for p1, p2 in zip(permutation, permutation[1:] + [permutation[0]]):
            if "me" in [p1, p2]:
                continue
            p_total += data[p1][p2]
            p_total += data[p2][p1]

        if p_total > max_happiness:
            max_happiness = p_total

    return max_happiness


print("Part 1:", part1())
print("Part 2:", part2())
