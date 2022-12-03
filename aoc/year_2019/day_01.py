def fuel_required(mass: int) -> int:
    return int(float(mass) / 3) - 2


total_fuel = 0
with open("input_01.txt") as f:
    for line in f.readlines():
        mass = int(line.strip())
        total_fuel += fuel_required(mass)

print("Part 1:", total_fuel)


total_fuel = 0
with open("input_01.txt") as f:
    for line in f.readlines():
        mass = int(line.strip())
        fuel = fuel_required(mass)
        total_fuel += fuel

        module_fuel_fuel_total = 0
        while True:
            fuel = fuel_required(fuel)
            if fuel < 0:
                break
            module_fuel_fuel_total += fuel
        total_fuel += module_fuel_fuel_total

print("Part 2:", total_fuel)
