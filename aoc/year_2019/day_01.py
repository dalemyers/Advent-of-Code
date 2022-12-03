def fuel_required(fuel_mass: int) -> int:
    return int(float(fuel_mass) / 3) - 2


total_fuel = 0
with open("input_01.txt", encoding="utf-8") as f:
    for line in f.readlines():
        mass = int(line.strip())
        total_fuel += fuel_required(mass)

print("Part 1:", total_fuel)


total_fuel = 0
with open("input_01.txt", encoding="utf-8") as f:
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
