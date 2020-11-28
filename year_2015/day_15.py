import itertools
import re


with open("year_2015/input_15.txt") as f:
    input_data = f.read()

# Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8
pattern = re.compile(r"(.*): capacity (-?\d*), durability (-?\d*), flavor (-?\d*), texture (-?\d*), calories (-?\d*)")

class Ingredient:

    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    @staticmethod
    def from_line(line):
        match = pattern.match(line)
        name = match.group(1)
        capacity = int(match.group(2))
        durability = int(match.group(3))
        flavor = int(match.group(4))
        texture = int(match.group(5))
        calories = int(match.group(6))
        return Ingredient(name, capacity, durability, flavor, texture, calories)

ingredients = []

for line in input_data.splitlines():
    ingredient = Ingredient.from_line(line)
    ingredients.append(ingredient)

def part1():
    best_score = 0
    best_ingredients = []

    for i1 in range(100):
        for i2 in range(100):
            if i1 + i2 > 100:
                break
            for i3 in range(100):
                if i1 + i2 + i3 > 100:
                    break
                i4 = 100 - (i1 + i2 + i3)

                capacity = (ingredients[0].capacity * i1) + (ingredients[1].capacity * i2) + (ingredients[2].capacity * i3) + (ingredients[3].capacity * i4)
                durability = (ingredients[0].durability * i1) + (ingredients[1].durability * i2) + (ingredients[2].durability * i3) + (ingredients[3].durability * i4)
                flavor = (ingredients[0].flavor * i1) + (ingredients[1].flavor * i2) + (ingredients[2].flavor * i3) + (ingredients[3].flavor * i4)
                texture = (ingredients[0].texture * i1) + (ingredients[1].texture * i2) + (ingredients[2].texture * i3) + (ingredients[3].texture * i4)

                capacity = max(capacity, 0)
                durability = max(durability, 0)
                flavor = max(flavor, 0)
                texture = max(texture, 0)

                score = capacity * durability * flavor * texture
                if score > best_score:
                    best_score = score
                    best_ingredients = [i1, i2, i3, i4]

    return best_score

def part2():
    best_score = 0
    best_ingredients = []

    for i1 in range(100):
        for i2 in range(100):
            if i1 + i2 > 100:
                break
            for i3 in range(100):
                if i1 + i2 + i3 > 100:
                    break
                i4 = 100 - (i1 + i2 + i3)

                calories = (ingredients[0].calories * i1) + (ingredients[1].calories * i2) + (ingredients[2].calories * i3) + (ingredients[3].calories * i4)
                if calories != 500:
                    continue

                capacity = (ingredients[0].capacity * i1) + (ingredients[1].capacity * i2) + (ingredients[2].capacity * i3) + (ingredients[3].capacity * i4)
                durability = (ingredients[0].durability * i1) + (ingredients[1].durability * i2) + (ingredients[2].durability * i3) + (ingredients[3].durability * i4)
                flavor = (ingredients[0].flavor * i1) + (ingredients[1].flavor * i2) + (ingredients[2].flavor * i3) + (ingredients[3].flavor * i4)
                texture = (ingredients[0].texture * i1) + (ingredients[1].texture * i2) + (ingredients[2].texture * i3) + (ingredients[3].texture * i4)

                capacity = max(capacity, 0)
                durability = max(durability, 0)
                flavor = max(flavor, 0)
                texture = max(texture, 0)

                score = capacity * durability * flavor * texture
                if score > best_score:
                    best_score = score
                    best_ingredients = [i1, i2, i3, i4]

    return best_score

print("Part 1:", part1())
print("Part 2:", part2())
