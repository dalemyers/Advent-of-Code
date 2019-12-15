
def fuel_required(mass: int) -> int:
    return int(float(mass) / 3) - 2


total_fuel = 0
with open("2019/01/input.txt") as f:
    for line in f.readlines():
        mass = int(line.strip())
        total_fuel += fuel_required(mass)

print(total_fuel)