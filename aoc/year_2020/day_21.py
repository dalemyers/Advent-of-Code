import copy
from collections import defaultdict
from shared import read_file_lines, is_int

contents = read_file_lines("year_2020/input_21.txt")


def get_foods():
    foods = []

    for line in contents:
        ingredients, allergens = line.split(" (")
        allergens = allergens[len("contains ") : -1]
        allergens = allergens.split(", ")
        ingredients = ingredients.split(" ")
        foods.append((set(ingredients), set(allergens)))

    return foods


def get_allergen_map(foods):
    allergen_map = defaultdict(list)

    for ingredients, allergens in foods:
        for ingredient in ingredients:
            for allergen in allergens:
                if ingredient not in allergen_map[allergen]:
                    allergen_map[allergen].append(ingredient)

    return allergen_map


def get_allergen_recipe_map(foods):
    allergen_map = defaultdict(list)
    for ingredients, allergens in foods:
        for allergen in allergens:
            allergen_map[allergen].append(set(ingredients))
    return allergen_map


def get_info():
    actuals = {}
    foods = get_foods()
    allergen_map = get_allergen_map(foods)
    allergen_recipe_map = get_allergen_recipe_map(foods)
    all_ingredients = set.union(*[food[0] for food in foods])
    known_allergens = {}
    potential_allergens = {}

    for allergen, recipes in allergen_recipe_map.items():
        common_ingredients = set.intersection(*recipes)
        if len(common_ingredients) == 1:
            known_allergens[allergen] = list(common_ingredients)[0]
        else:
            if potential_allergens.get(allergen) is None:
                potential_allergens[allergen] = set()
            potential_allergens[allergen] = potential_allergens[allergen].union(common_ingredients)

    changes = True
    while changes:
        changes = False

        for allergen, ingredient in known_allergens.items():
            for (
                potential_allergen,
                potential_ingredients,
            ) in potential_allergens.items():
                if ingredient in potential_ingredients:
                    changes = True
                    potential_ingredients.remove(ingredient)

        to_delete = []
        for allergen, ingredients in potential_allergens.items():
            if len(ingredients) != 1:
                continue

            known_allergens[allergen] = list(ingredients)[0]
            to_delete.append(allergen)

        for allergen in to_delete:
            changes = True
            del potential_allergens[allergen]

    counter = 0
    allergen_ingredients = set(known_allergens.values())
    for ingredients, _ in foods:
        for ingredient in ingredients:
            if ingredient not in allergen_ingredients:
                counter += 1

    return counter, known_allergens


def part1():
    counter, _ = get_info()
    return counter


def part2():
    _, known_allergens_dict = get_info()

    known_allergens = [(k, v) for k, v in known_allergens_dict.items()]
    known_allergens.sort(key=lambda x: x[0])

    ingredients = ",".join([x[1] for x in known_allergens])
    return ingredients


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
