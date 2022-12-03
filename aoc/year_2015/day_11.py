import itertools
import sys

password = list("cqjxjnds")

printed = 0

while True:
    password[-1] = chr(ord(password[-1]) + 1)
    index = 0
    while True:
        index -= 1
        if abs(index) > len(password):
            break
        if password[index] == "{":
            password[index] = "a"
            password[index - 1] = chr(ord(password[index - 1]) + 1)
        else:
            break
    if "i" in password:
        continue
    if "o" in password:
        continue
    if "l" in password:
        continue

    has_sequence = False
    for i in range(len(password) - 2):
        substring = password[i : i + 3]
        if ord(substring[0]) + 1 == ord(substring[1]) and ord(substring[0]) + 2 == ord(
            substring[2]
        ):
            has_sequence = True
            break

    if not has_sequence:
        continue

    pair1 = None
    has_pair = False
    for a, b in zip(password, password[1:]):
        if a != b:
            continue
        if pair1 is None:
            pair1 = a
            continue
        if a != pair1:
            has_pair = True
            break

    if not has_pair:
        continue

    print(f"Part {printed + 1}:", "".join(password))
    printed += 1

    if printed >= 2:
        break
