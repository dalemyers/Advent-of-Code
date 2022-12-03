import enum
import itertools


class ItemType(enum.Enum):
    weapon = 1
    armor = 2
    ring = 3


class Item:
    def __init__(self, name, cost, damage, armor, item_type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor
        self.item_type = item_type

    def __repr__(self):
        return f"{self.name}({self.cost}, {self.damage}, {self.armor})"

    def __str__(self):
        return self.__repr__()


weapons = [
    Item("Dagger", 8, 4, 0, ItemType.weapon),
    Item("Shortsword", 10, 5, 0, ItemType.weapon),
    Item("Warhammer", 25, 6, 0, ItemType.weapon),
    Item("Longsword", 40, 7, 0, ItemType.weapon),
    Item("Greataxe", 74, 8, 0, ItemType.weapon),
]

armors = [
    Item("None", 0, 0, 0, ItemType.armor),
    Item("Leather", 13, 0, 1, ItemType.armor),
    Item("Chainmail", 31, 0, 2, ItemType.armor),
    Item("Splintmail", 53, 0, 3, ItemType.armor),
    Item("Bandedmail", 75, 0, 4, ItemType.armor),
    Item("Platemail", 102, 0, 5, ItemType.armor),
]

rings = [
    Item("Damage +1", 25, 1, 0, ItemType.ring),
    Item("Damage +2", 50, 2, 0, ItemType.ring),
    Item("Damage +3", 100, 3, 0, ItemType.ring),
    Item("Defense +1", 20, 0, 1, ItemType.ring),
    Item("Defense +2", 40, 0, 2, ItemType.ring),
    Item("Defense +3", 80, 0, 3, ItemType.ring),
]


def fight(hp, damage, armor, boss_hp=103, boss_damage=9, boss_armor=2):
    while True:
        boss_hp -= max(damage - boss_armor, 1)
        if boss_hp <= 0:
            return True
        hp -= max(boss_damage - armor, 1)
        if hp <= 0:
            return False


def part1():
    min_cost = 99999999999

    for weapon in weapons:
        for armor in armors:
            for ring_selection in itertools.chain(
                itertools.permutations(rings, 1), itertools.permutations(rings, 2)
            ):
                cost = weapon.cost + armor.cost + sum([ring.cost for ring in ring_selection])
                damage = (
                    weapon.damage + armor.damage + sum([ring.damage for ring in ring_selection])
                )
                tarmor = weapon.armor + armor.armor + sum([ring.armor for ring in ring_selection])

                if fight(100, damage, tarmor):
                    if cost < min_cost:
                        min_cost = cost

    return min_cost


def part2():
    max_cost = 0

    for weapon in weapons:
        for armor in armors:
            for ring_selection in itertools.chain(
                itertools.permutations(rings, 1), itertools.permutations(rings, 2)
            ):
                cost = weapon.cost + armor.cost + sum([ring.cost for ring in ring_selection])
                damage = (
                    weapon.damage + armor.damage + sum([ring.damage for ring in ring_selection])
                )
                tarmor = weapon.armor + armor.armor + sum([ring.armor for ring in ring_selection])

                if not fight(100, damage, tarmor):
                    if cost > max_cost:
                        max_cost = cost

    return max_cost


print("Part 1:", part1())
print("Part 2:", part2())
