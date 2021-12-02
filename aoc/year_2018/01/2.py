import sys

frequencies = {}
frequency = 0

with open('01/input.txt') as input_file:
    deltas = [int(line) for line in input_file.readlines()]

while True:
    for delta in deltas:
        frequency += delta

        if frequencies.get(frequency, False):
            print(frequency)
            sys.exit(0)

        frequencies[frequency] = True
