import functools
from shared import read_file_lines

contents = read_file_lines("year_2020/input_07.txt")

def parse_bag(bag_text):
    """
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    """
    components = bag_text.split(" bags contain ")
    color = components[0]
    contents = [c.strip() for c in components[1][:-1].split(",")]
    parsed_contents = []
    for bag in contents:
        if bag.endswith("."):
            bag = bag[:-1]
        if bag.endswith("s"):
            bag = bag[:-1]
        if bag == "no other bag":
            continue
        bag = bag[:-4]
        bag_components = bag.split(" ")
        bag_count = int(bag_components[0])
        bag_color = " ".join(bag_components[1:])
        parsed_contents.append((bag_count, bag_color))

    return (color, parsed_contents)


def get_bags():
    bags = {}
    for line in contents:
        bag = parse_bag(line)
        bags[bag[0]] = bag[1]
    return bags


BAGS = get_bags()


def bag_contains(color, containers):
    for container in containers:
        if container[1] == color:
            return True
    for container in containers:
        subcontainers = BAGS[container[1]]
        if bag_contains(color, subcontainers):
            return True
    return False


@functools.lru_cache(maxsize=2048)
def bag_count(color):
    total = 0
    subs = BAGS[color]
    for count, subbag in subs:
        total += count
        total += count * bag_count(subbag)
    return total


def part1():

    count = 0
    for color, containers in BAGS.items():
        if bag_contains("shiny gold", containers):
            count += 1
    return count

def part2():
    return bag_count("shiny gold")


print("Part 1:", part1())
print("Part 2:", part2())
