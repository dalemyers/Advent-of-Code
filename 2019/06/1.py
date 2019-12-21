with open("2019/06/input.txt") as f:
    full_input = f.read().strip()

orbit_list = list(map(lambda x: x.split(")"), full_input.split("\n")))
print(orbit_list)

orbits = {}

for a, b in orbit_list:
    # b orbits around a
    orbits[b] = a

orbit_count = 0

for root_orbiter, root_center in orbits.items():
    orbit_count += 1

    orbiter = root_orbiter
    center = root_center
    while True:
        if center in orbits:
            orbiter = center
            center = orbits[center]
            orbit_count += 1
        else:
            break

print(orbit_count)