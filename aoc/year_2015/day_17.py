from shared import read_ints_from_file


def solve(sizes, target_size):

    # This will hold our running total as we go. Each new item on the stack
    # contains the size of the current item, and the total size so far
    stack = [(0, sizes[0])]

    # For part 1, a counter is enough, but for part 2 we need to track the
    # containers we used
    combinations = []

    while True:
        index, size = stack[-1]
        next_index = index + 1

        # Check if the size of what we have so far is less than the target
        if size < target_size:

            # It was smaller, so we need to add at least one more container

            # If there's a next one, let's just add it and repeat
            if next_index < len(sizes):
                # add the next smallest container
                stack.append((next_index, size + sizes[next_index]))
                continue

            # There was nothing left to add, so let's back track by getting rid
            # of the second smallest container, and replacing it with something
            # smaller
            stack.pop()

            # If we've run out of things on the stack, we have exhausted all
            # possible solutions
            if len(stack) == 0:
                break

            # Perform the replacement
            index, size = stack.pop()
            new_index = index + 1
            new_size = size - sizes[index] + sizes[new_index]
            stack.append((new_index, new_size))
            continue

        # We know that the size is now either the same or larger than the target

        # If it is the same, we track it
        if size == target_size:
            combinations.append([item[0] for item in stack])

        # Either way, if it was bigger or the same, we are done with it, so we
        # get rid of it, and move onto the next index
        index, size = stack.pop()
        new_index = index + 1

        # If we are at the end of the list of sizes, ?
        if new_index == len(sizes):
            index, size = stack.pop()
            new_index = index + 1

        # The new size is going to be the current size, minius the size of the
        # one we just got rid of, plus the new size.
        new_size = size - sizes[index] + sizes[new_index]
        stack.append((new_index, new_size))

    combinations.sort()
    lowest = min(map(len, combinations))
    count = len(
        [combination for combination in combinations if len(combination) == lowest]
    )
    return len(combinations), count


all_sizes = read_ints_from_file("year_2015/input_17.txt")
all_sizes.sort(reverse=True)

part1, part2 = solve(all_sizes, 150)
print("Part 1:", part1)
print("Part 2:", part2)
