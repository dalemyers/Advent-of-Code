puzzle_input = (353096, 843212)

possibilities = []

for i in range(puzzle_input[0], puzzle_input[1] + 1):
    string_value = str(i)
    previous_value = -1
    has_double = False
    should_continue = False

    # Going from left to right, the digits never decrease; they only ever
    # increase or stay the same (like 111123 or 135679).
    for character in string_value:
        character_value = int(character)
        if character_value < previous_value:
            should_continue = True
            break

        # Two adjacent digits are the same (like 22 in 122345).
        if character_value == previous_value:
            has_double = True

        previous_value = character_value

    if not has_double:
        should_continue = True

    if should_continue:
        continue

    possibilities.append(i)

print(len(possibilities))