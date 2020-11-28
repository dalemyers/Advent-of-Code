
with open("year_2015/input_05.txt") as f:
    contents = f.read()

nice_count = 0

for string in contents.splitlines():
    vowel_count = 0
    last_letter = None
    has_double = False

    for character in string:
        if character in "aeiou":
            vowel_count += 1
        if character == last_letter:
            has_double = True
        last_letter = character

    banned = False
    for s in ["ab", "cd", "pq", "xy"]:
        if s in string:
            banned = True
            break

    if vowel_count >= 3 and has_double and not banned:
        nice_count += 1

print("Part 1:", nice_count)

nice_count = 0

for string in contents.splitlines():
    has_pair = False
    has_next_gap = False

    for index in range(0, len(string) - 1):
        pair = string[index:index + 2]
        left = string[:index]
        right = string[index + 2:]
        l_pos = left.find(pair)
        r_pos = right.find(pair)
        if l_pos != -1 or r_pos != -1:
            has_pair = True
        if index < len(string) - 2 and string[index] == string[index + 2]:
            has_next_gap = True
        if has_pair and has_next_gap:
            break

    if has_pair and has_next_gap:
        nice_count += 1

print("Part 2:", nice_count)