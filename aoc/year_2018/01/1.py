offset = 0

with open("01/input.txt", encoding="utf-8") as input_file:
    for line in input_file.readlines():
        offset += int(line)

print(offset)
