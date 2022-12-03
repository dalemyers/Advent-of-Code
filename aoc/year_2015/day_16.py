import itertools
import re


with open("year_2015/input_16.txt") as f:
    input_data = f.read()


class Sue:
    def __init__(
        self,
        *,
        children=-1,
        cats=-1,
        samoyeds=-1,
        pomeranians=-1,
        akitas=-1,
        vizslas=-1,
        goldfish=-1,
        trees=-1,
        cars=-1,
        perfumes=-1
    ):
        self.facts = {}
        self.facts["children"] = children
        self.facts["cats"] = cats
        self.facts["samoyeds"] = samoyeds
        self.facts["pomeranians"] = pomeranians
        self.facts["akitas"] = akitas
        self.facts["vizslas"] = vizslas
        self.facts["goldfish"] = goldfish
        self.facts["trees"] = trees
        self.facts["cars"] = cars
        self.facts["perfumes"] = perfumes

    def matches(self) -> bool:
        if self.facts["children"] not in [3, -1]:
            return False
        if self.facts["cats"] not in [7, -1]:
            return False
        if self.facts["samoyeds"] not in [2, -1]:
            return False
        if self.facts["pomeranians"] not in [3, -1]:
            return False
        if self.facts["akitas"] not in [0, -1]:
            return False
        if self.facts["vizslas"] not in [0, -1]:
            return False
        if self.facts["goldfish"] not in [5, -1]:
            return False
        if self.facts["trees"] not in [3, -1]:
            return False
        if self.facts["cars"] not in [2, -1]:
            return False
        if self.facts["perfumes"] not in [1, -1]:
            return False
        return True

    def matches2(self) -> bool:
        if self.facts["children"] not in [3, -1]:
            return False
        if self.facts["samoyeds"] not in [2, -1]:
            return False
        if self.facts["akitas"] not in [0, -1]:
            return False
        if self.facts["vizslas"] not in [0, -1]:
            return False
        if self.facts["cars"] not in [2, -1]:
            return False
        if self.facts["perfumes"] not in [1, -1]:
            return False
        if self.facts["cats"] != -1 and self.facts["cats"] <= 7:
            return False
        if self.facts["trees"] != -1 and self.facts["trees"] <= 3:
            return False
        if self.facts["pomeranians"] != -1 and self.facts["pomeranians"] >= 3:
            return False
        if self.facts["goldfish"] != 1 and self.facts["goldfish"] >= 5:
            return False
        return True


sues = []

for line in input_data.splitlines():
    # Sue 279: cars: 6, pomeranians: 8, trees: 2
    match = re.match(r"Sue (\d*): (.*)", line)
    number = int(match.group(1))
    items_str = match.group(2)
    items = items_str.split(", ")
    items_dict = {}
    for item in items:
        name, value = item.split(": ")
        items_dict[name] = int(value)
    sues.append(Sue(**items_dict))


print("Part 1:", [index + 1 for index, sue in enumerate(sues) if sue.matches()][0])
print("Part 2:", [index + 1 for index, sue in enumerate(sues) if sue.matches2()][0])
