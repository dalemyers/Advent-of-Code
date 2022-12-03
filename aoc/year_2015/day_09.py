import itertools
import sys


with open("year_2015/input_09.txt") as f:
    contents = f.read()

distances = {}


for line in contents.splitlines():
    # Tristram to Snowdin = 100
    places, distance = line.split(" = ")
    a, b = places.split(" to ")
    distance = int(distance)
    if distances.get(a) is None:
        distances[a] = {}
    if distances.get(b) is None:
        distances[b] = {}
    distances[a][b] = distance
    distances[b][a] = distance

places = set()

for place in distances.keys():
    places.add(place)
    dests = distances[place].keys()
    for dest in dests:
        places.add(dest)

places = list(places)

routes = list(itertools.permutations(places))

min_dist = sys.maxsize
max_dist = 0

for route in routes:
    distance = 0
    for a, b in zip(route, route[1:]):
        distance += distances[a][b]
    if distance < min_dist:
        min_dist = distance
    if distance > max_dist:
        max_dist = distance

print("Part 1:", min_dist)
print("Part 2:", max_dist)
