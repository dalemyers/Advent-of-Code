import sys


def check(ids):
    for one in ids:
        for two in ids:
            position = None
            for i in range(len(one)):
                if one[i] != two[i]:
                    if position is not None:
                        position = None
                        break
                    position = i
            if position is not None:
                print(one[:position] + one[position+1:])
                sys.exit(1)


with open('02/input.txt') as input_file:
    ids = [line.strip() for line in input_file.readlines()]


check(ids)