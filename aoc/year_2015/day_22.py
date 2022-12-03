import enum
import itertools


class Spell:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __repr__(self):
        return f"{self.name}({self.cost})"

    def __str__(self):
        return self.__repr__()


class Fighter:
    def __init__(self, hp):
        self.hp = hp

    def is_alive(self):
        return self.hp > 0


class Player(Fighter):
    def __init__(self, hp, mana, armor=0):
        self.mana = mana
        self.armor = armor
        super().__init__(hp)

    def copy(self):
        return Player(self.hp, self.mana, self.armor)

    def __repr__(self):
        return f"Player({self.hp}, {self.mana}, {self.armor})"

    def __str__(self):
        return self.__repr__()


class Boss(Fighter):
    def __init__(self, hp, damage):
        self.damage = damage
        super().__init__(hp)

    def copy(self):
        return Boss(self.hp, self.damage)

    def __repr__(self):
        return f"Boss({self.hp}, {self.damage})"

    def __str__(self):
        return self.__repr__()


class Effect:
    def __init__(self, duration):
        self.duration = duration

    def remove(self, player, boss):
        pass


class ShieldEffect(Effect):
    def __init__(self, remaining_duration=6, has_applied=False):
        self.spell_name = "Shield"
        self.has_applied = has_applied
        super().__init__(remaining_duration)

    def turn_start(self, player, boss):
        self.duration -= 1
        if not self.has_applied:
            self.has_applied = True
            player.armor += 7
        # print(f"Shield's timer is now {self.duration}.")

    def remove(self, player, boss):
        player.armor -= 7

    def copy(self):
        return ShieldEffect(remaining_duration=self.duration, has_applied=self.has_applied)


class PoisonEffect(Effect):
    def __init__(self, remaining_duration=6):
        self.spell_name = "Poison"
        super().__init__(remaining_duration)

    def turn_start(self, player, boss):
        boss.hp -= 3
        self.duration -= 1
        # print(f"Poison deals 3 damage; its timer is now {self.duration}.")

    def copy(self):
        return PoisonEffect(remaining_duration=self.duration)


class RechargeEffect(Effect):
    def __init__(self, remaining_duration=5):
        self.spell_name = "Recharge"
        super().__init__(remaining_duration)

    def turn_start(self, player, boss):
        player.mana += 101
        self.duration -= 1
        # print(f"Recharge provides 101 mana; its timer is now {self.duration}.")

    def copy(self):
        return RechargeEffect(remaining_duration=self.duration)


magic_missile = Spell("Magic Missile", 53)
drain = Spell("Drain", 73)
shield = Spell("Shield", 113)
poison = Spell("Poison", 173)
recharge = Spell("Recharge", 229)

spells = [magic_missile, drain, shield, poison, recharge]

damage = {
    "Magic Missile": 4,
    "Drain": 2,
}

healing = {"Drain": 2}


class State:
    def __init__(self, player, boss, effects):
        self.player = player.copy()
        self.boss = boss.copy()
        self.effects = [effect.copy() for effect in effects]

    def __repr__(self):
        return f"State({self.player}, {self.boss}, {self.effects})"

    def __str__(self):
        return self.__repr__()


def play(per_turn_loss=0):
    stack = [(0, 0, State(Player(50, 500), Boss(58, 9), []))]

    solution = 99999999999999999999

    while len(stack) > 0:

        base_mana_spent, choices, base_state = stack.pop()

        for spell in spells:

            skip = False
            for effect in base_state.effects:
                if spell.name == effect.spell_name and effect.duration > 1:
                    skip = True
                    break

            if skip:
                continue

            mana_spent = base_mana_spent

            if mana_spent + spell.cost > solution:
                continue

            player = base_state.player.copy()
            boss = base_state.boss.copy()
            effects = [effect.copy() for effect in base_state.effects]

            # print(f"-- Player turn ({choices}) --")
            # print(f"- Player has {player.hp} hit points, {player.armor} armor, {player.mana} mana")
            # print(f"- Boss has {boss.hp} hit points")

            # Player turn start

            if per_turn_loss:
                player.hp -= 1

            if not player.is_alive():
                continue

            for effect in effects:
                effect.turn_start(player, boss)

            if not boss.is_alive():
                solution = min(solution, mana_spent)
                continue

            if spell.cost > player.mana:
                continue

            # print(f"Player casts {spell.name}")
            mana_spent += spell.cost
            # print()

            player.mana -= spell.cost
            player.hp += healing.get(spell.name, 0)
            boss.hp -= damage.get(spell.name, 0)
            if not boss.is_alive():
                solution = min(solution, mana_spent)
                continue

            ended_effects = [effect for effect in effects if effect.duration <= 0]
            for effect in ended_effects:
                effect.remove(player, boss)
            effects = [effect for effect in effects if effect.duration > 0]

            if spell == shield:
                effect = ShieldEffect()
            elif spell == poison:
                effect = PoisonEffect()
            elif spell == recharge:
                effect = RechargeEffect()
            else:
                effect = None

            if effect:
                effects.append(effect)

            # Player turn end
            # Boss turn start

            # print("-- Boss turn --")
            # print(f" - Player has {player.hp} hit points, {player.armor} armor, {player.mana} mana")
            # print(f" - Boss has {boss.hp} hit points")

            for effect in effects:
                effect.turn_start(player, boss)

            if not boss.is_alive():
                solution = min(solution, mana_spent)
                continue

            boss_damage = max(boss.damage - player.armor, 1)
            player.hp -= boss_damage
            # print(f"Boss attacks for {boss_damage} damage")
            # print()

            if not player.is_alive():
                continue

            ended_effects = [effect for effect in effects if effect.duration <= 0]
            for effect in ended_effects:
                effect.remove(player, boss)
            effects = [effect for effect in effects if effect.duration > 0]

            # Boss turn end

            stack.append((mana_spent, choices + 1, State(player, boss, effects)))

    return solution


def part1():
    return play()


def part2():
    return play(1)


print("Part 1:", part1())
print("Part 1:", part2())
