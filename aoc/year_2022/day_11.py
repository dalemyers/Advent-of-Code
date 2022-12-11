"""Day 11"""

import enum
from typing import List
from aoc.shared import read_chunked

DEBUG = False
chunks = read_chunked("year_2022/input_11.txt")


class Operation(enum.Enum):
    ADD = "+"
    MULTIPLY = "*"

    def text(self) -> str:
        if self == Operation.ADD:
            return "increases by"
        return "is multiplied by"


class Monkey:

    items: List[int]
    operation: Operation
    operand: str
    divisible_by: int
    true_monkey: int
    false_monkey: int
    inspections: int

    def __init__(
        self,
        starting_items: List[int],
        operation: Operation,
        operand: str,
        divisible_by: int,
        true_monkey: int,
        false_monkey: int,
    ) -> None:
        self.items = starting_items
        self.operation = operation
        self.operand = operand
        self.divisible_by = divisible_by
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspections = 0

    def __repr__(self) -> str:
        return f"<Monkey items={self.items}>"

    @staticmethod
    def from_string(raw: str) -> "Monkey":
        lines = raw.split("\n")
        lines.pop(0)  # Drop identifier

        lines = [l[2:] for l in lines]

        starting_items = list(
            map(int, lines.pop(0).replace("Starting items: ", "").split(", "))
        )
        raw_operation = lines.pop(0).replace("Operation: new = old ", "")
        operation = Operation(raw_operation[0])
        raw_operation = raw_operation[2:]
        operand = raw_operation

        divisible_by = int(lines.pop(0).replace("Test: divisible by ", ""))
        true_monkey = int(lines.pop(0).replace("  If true: throw to monkey ", ""))
        false_monkey = int(lines.pop(0).replace("  If false: throw to monkey ", ""))

        return Monkey(
            starting_items, operation, operand, divisible_by, true_monkey, false_monkey
        )


def load_monkeys() -> List[Monkey]:
    monkeys = []
    for raw_monkey in chunks:
        monkeys.append(Monkey.from_string(raw_monkey))
    return monkeys


def log(string: str) -> None:
    if DEBUG is True:
        print(string)


def perform_monkey_business(rounds: int, reduce_worry: bool) -> int:
    monkeys = load_monkeys()

    factor = 1
    for monkey in monkeys:
        factor = factor * monkey.divisible_by

    for round_iteration in range(rounds):
        print(f"Round {round_iteration}")
        for index, monkey in enumerate(monkeys):
            log(f"Monkey {index}:")
            for item in monkey.items:
                if reduce_worry:
                    worry_level = item
                else:
                    worry_level = item % factor

                log(f"  Monkey inspects an item with a worry level of {worry_level}.")
                monkey.inspections += 1

                if monkey.operand == "old":
                    value = worry_level
                else:
                    value = int(monkey.operand)

                if monkey.operation == Operation.ADD:
                    worry_level += value
                else:
                    worry_level *= value

                log(
                    f"    Worry level {monkey.operation.text()} {value} to {worry_level}"
                )

                if reduce_worry:
                    worry_level = int(worry_level / 3.0)
                    log(
                        f"    Monkey gets bored with item. Worry level is divided by 3 to {worry_level}."
                    )

                if worry_level % monkey.divisible_by == 0:
                    log(
                        f"    Current worry level is divisible by {monkey.divisible_by}."
                    )
                    log(
                        f"    Item with worry level {worry_level} is thrown to monkey {monkey.true_monkey}."
                    )
                    monkeys[monkey.true_monkey].items.append(worry_level)
                else:
                    log(
                        f"    Current worry level is not divisible by {monkey.divisible_by}."
                    )
                    log(
                        f"    Item with worry level {worry_level} is thrown to monkey {monkey.false_monkey}."
                    )
                    monkeys[monkey.false_monkey].items.append(worry_level)

            monkey.items = []

    values = sorted(list(map(lambda m: m.inspections, monkeys)), reverse=True)

    return values[0] * values[1]


def part1() -> int:
    """Part 1."""
    return perform_monkey_business(20, reduce_worry=True)


def part2() -> int:
    """Part 2."""
    return perform_monkey_business(10000, reduce_worry=False)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
