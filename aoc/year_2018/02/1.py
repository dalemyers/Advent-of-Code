class Counter:
    def __init__(self):
        self.internal = {}

    def count(self, value):
        if self.internal.get(value) is None:
            self.internal[value] = 0

        self.internal[value] += 1


two_counts = 0
three_counts = 0

with open("02/input.txt", encoding="utf-8") as input_file:
    for line in input_file.readlines():
        line = line.strip()
        counter = Counter()
        for character in line:
            counter.count(character)
        values = set(counter.internal.values())
        if 2 in values:
            two_counts += 1
        if 3 in values:
            three_counts += 1

print(two_counts, three_counts)
print(two_counts * three_counts)
