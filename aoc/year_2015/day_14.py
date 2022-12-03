import re


with open("year_2015/input_14.txt", encoding="utf-8") as f:
    input_data = f.read()

# Prancer can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
pattern = re.compile(
    r"(.*) can fly (\d*) km\/s for (\d*) seconds, but then must rest for (\d*) seconds\."
)


class Reindeer:
    def __init__(self, name, speed, duration, rest_time):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest_time = rest_time
        self.distance_travelled = 0
        self.remaining_duration = duration
        self.remaining_rest = rest_time

    def increment(self):
        if self.remaining_duration > 0:
            self.distance_travelled += self.speed
            self.remaining_duration -= 1
            self.remaining_rest = self.rest_time
            return

        if self.remaining_duration == 0:
            if self.remaining_rest == 0:
                self.remaining_duration = self.duration
                self.increment()
            else:
                self.remaining_rest -= 1
            return

    @staticmethod
    def from_line(line):
        match = pattern.match(line)
        name = match.group(1)
        speed = int(match.group(2))
        duration = int(match.group(3))
        rest_time = int(match.group(4))
        return Reindeer(name, speed, duration, rest_time)


reindeers = {}
scores = {}

for entry in input_data.splitlines():
    reindeer = Reindeer.from_line(entry)
    reindeers[reindeer.name] = reindeer
    scores[reindeer.name] = 0

for i in range(2503):
    print(i, end=" | ")
    best_distance = 0
    for rname, reindeer in reindeers.items():
        reindeer.increment()
        print(rname, reindeer.distance_travelled, end=" | ")
        if reindeer.distance_travelled > best_distance:
            best_distance = reindeer.distance_travelled
    print()

    print(i, end=" | ")
    for rname, reindeer in reindeers.items():
        if reindeer.distance_travelled == best_distance:
            scores[rname] += 1
        print(rname, scores[rname], end=" | ")
    print()

print(
    "Part 1:",
    sorted(
        [(r.name, r.distance_travelled) for r in reindeers.values()],
        key=lambda x: -x[1],
    )[0][1],
)
print("Part 2:", sorted(list(scores.values()), reverse=True)[0])
