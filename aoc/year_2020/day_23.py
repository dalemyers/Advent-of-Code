from shared import read_file_lines

input_labels = list(map(int, read_file_lines("year_2020/input_23.txt")[0]))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def get_output(nodes, current_node):
    output = []
    first_node = nodes
    n = nodes
    while True:
        if n is current_node:
            output.append(f"({n.value})")
        else:
            output.append(str(n.value))
        n = n.next
        if n == first_node:
            break
    return " ".join(output)


def get_n_nodes(nodes, n):
    output = []
    current = nodes
    while len(output) < n:
        output.append(current)
        current = current.next
    return output


def move(i, should_log, should_log_verbose, current_node, node_map, highest, lowest):
    if should_log:
        print(f"-- move {i} --")
        if should_log_verbose:
            print("cups:", get_output(node_map[1], current_node))

    # Get the next 3 cups
    picked_up = [current_node.next, current_node.next.next, current_node.next.next.next]

    if should_log_verbose:
        print("picked up:", [n.value for n in picked_up])

    x = """
    label = current_node.value - 1
    while True:
        if label < lowest:
            label = highest

        destination = node_map[label]

        if destination in picked_up:
            label -= 1
            continue

        break
"""
    label = current_node.value - 1
    destination = None

    while label > 0 and destination is None:
        if label not in picked_up:
            destination = node_map[label]
        label -= 1

    max_label = highest
    while destination is None:
        if max_label not in picked_up:
            destination = node_map[max_label]
        max_label -= 1
    ###

    destination_successor = destination.next
    destination.next = picked_up[0]
    current_node.next = picked_up[-1].next
    picked_up[-1].next = destination_successor

    return current_node.next


def run(max_moves, node_extension):
    cup_list = input_labels[:]
    lowest = min(cup_list)
    highest = max(cup_list)

    if node_extension:
        cup_list = cup_list + list(range(highest + 1, node_extension + 1))

    nodes = [Node(v) for v in cup_list]
    for i in range(0, len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    nodes[len(cup_list) - 1].next = nodes[0]

    node_map = {v: nodes[n] for n, v in enumerate(cup_list)}

    if node_extension:
        highest = node_extension

    current_node = nodes[0]

    for i in range(0, max_moves):
        current_node = move(i, i % 10_000 == 0, False, current_node, node_map, highest, lowest)
        if current_node.value == 814631:  # 1870830 1870833
            breakpoint()

    return current_node, node_map


def part1():
    current_node, node_map = run(100, None)
    return get_output(node_map[1].next, None).replace(" ", "")[:-1]


def part2():
    current_node, node_map = run(10_000_000, 1_000_000)
    return current_node.next.value * current_node.next.next.value


if __name__ == "__main__":
    # print("Part 1:", part1())
    print("Part 2:", part2())
