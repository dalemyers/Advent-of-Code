with open("2019/06/input.txt") as f:
    full_input = f.read().strip()

orbit_list = list(map(lambda x: x.split(")"), full_input.split("\n")))

orbits = {}

for a, b in orbit_list:
    # b orbits around a
    orbits[b] = a

our_key = "YOU"
our_path = [our_key]

while True:
    our_key = orbits.get(our_key)
    if our_key is None:
        break
    our_path.append(our_key)

santa_key = "SAN"
santa_path = [santa_key]

while True:
    santa_key = orbits.get(santa_key)
    if santa_key is None:
        break
    santa_path.append(santa_key)

our_path.reverse()
santa_path.reverse()

count = 0

for us, santa in zip(our_path, santa_path):
    if us != santa:
        break
    count += 1

our_path = our_path[count:]
santa_path = santa_path[count:]

print(count)
print(our_path)
print(santa_path)

print(len(our_path) + len(santa_path) - 2)