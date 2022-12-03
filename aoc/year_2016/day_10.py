import enum
import re
from shared import read_file_lines

contents = read_file_lines("year_2016/input_10.txt")


class Location(enum.Enum):
    bot = 1
    output = 2


class Bot:
    def __init__(self):
        self.values = []

    def add_value(self, location, value):
        if len(self.values) < 2:
            self.values.append((value, location))
        else:
            raise Exception()
        self.values.sort()

    def high(self):
        try:
            return self.values[-1]
        except IndexError:
            return None

    def low(self):
        try:
            return self.values[0]
        except IndexError:
            return None

    def __repr__(self):
        return f"Bot({self.low()}, {self.high()})"

    def __str__(self):
        return self.__repr__()


class ValueInstruction:
    def __init__(self, value, bot):
        self.value = value
        self.bot = bot

    @staticmethod
    def from_line(line):
        line = line[len("value ") :]
        values = list(map(int, line.split(" goes to bot ")))
        return ValueInstruction(*values)


class GiveInstruction:
    def __init__(self, holder, low, high):
        self.holder = holder
        self.low = low
        self.high = high

    def bots(self):
        output = [self.holder]
        if self.low.startswith("bot "):
            output.append(int(self.low[5:]))
        if self.high.startswith("bot "):
            output.append(int(self.high[5:]))
        return output

    def outputs(self):
        output = []
        if self.low[0] == Location.output:
            output.append(int(self.low[1]))
        if self.high[0] == Location.output:
            output.append(int(self.high[1]))
        return output

    @staticmethod
    def from_line(line):
        match = re.match(r"bot (\d*) gives low to (.*) and high to (.*)", line)
        assert match
        bot_id = int(match.group(1))
        low = match.group(2)
        high = match.group(3)
        if low.startswith("output "):
            low = (Location.output, int(low[7:]))
        else:
            low = (Location.bot, int(low[4:]))
        if high.startswith("output "):
            high = (Location.output, int(high[7:]))
        else:
            high = (Location.bot, int(high[4:]))
        return GiveInstruction(bot_id, low, high)


def part1():
    starting_conditions = []
    outputs = {}
    bots = {}
    instructions = []
    for line in contents:
        if line.startswith("value "):
            starting_conditions.append(ValueInstruction.from_line(line))
        else:
            instruction = GiveInstruction.from_line(line)
            instructions.append(instruction)

    for instruction in instructions:
        for output in instruction.outputs():
            outputs[output] = None
        for bot in instruction.outputs():
            if bots.get(bot) is None:
                bots[bot] = Bot()

    for starting_condition in starting_conditions:
        bots[starting_condition.bot].add_value(None, starting_condition.value)

    for instruction in instructions:
        bot = bots[instruction.holder]
        low = bot.low()
        high = bot.high()
        bot.values = []

        if low is not None:
            if low[1] == Location.output:
                outputs[low[0]] = bot.low()
            elif low[1] == Location.bot:
                bots[low[0]].add_value(bot.low())

        if high is not None:
            if high[1] == Location.output:
                outputs[high[0]] = bot.high()
            elif high[1] == Location.bot:
                bots[high[0]].add_value(bot.high())

    print()


def part2():
    pass


print("Part 1:", part1())
print("Part 2:", part2())
