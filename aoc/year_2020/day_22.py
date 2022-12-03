from shared import read_file_lines

contents = read_file_lines("year_2020/input_22.txt")


def get_decks():
    player1 = []
    current_player = []
    for line in contents:
        if len(line.strip()) == 0:
            continue
        if line.startswith("Player 1:"):
            continue
        if line.startswith("Player 2:"):
            player1 = current_player
            current_player = []
            continue
        current_player.append(int(line))
    return player1, current_player


def play_combat(p1, p2):
    counter = 0
    while len(p1) != 0 and len(p2) != 0:
        counter += 1
        print(f"-- Round {counter} --")
        print(f"Player 1's deck: " + ", ".join(map(str, p1)))
        print(f"Player 2's deck: " + ", ".join(map(str, p2)))
        p1_top = p1.pop(0)
        p2_top = p2.pop(0)
        print(f"Player 1 plays: {p1_top}")
        print(f"Player 2 plays: {p2_top}")
        if p1_top > p2_top:
            print("Player 1 wins the round!")
            p1.append(p1_top)
            p1.append(p2_top)
        else:
            print("Player 2 wins the round!")
            p2.append(p2_top)
            p2.append(p1_top)
        print()

    print()
    print("== Post-game results ==")
    print(f"Player 1's deck: " + ", ".join(map(str, p1)))
    print(f"Player 2's deck: " + ", ".join(map(str, p2)))

    return p1, p2


def calculate_score(deck):
    total = 0
    for index, value in enumerate(deck):
        positional_value = len(deck) - index
        total += positional_value * value
    return total


class States:
    def __init__(self, states=None, player_indices=None):
        if states:
            self.states = states
        else:
            self.states = []

        if player_indices:
            self.player_indices = player_indices
        else:
            self.player_indices = []

    def lookup_state(self, deck, player):
        try:
            index = self.states.index(deck)
        except ValueError:
            return False
        return self.player_indices[index] == player

    def add_state(self, deck, player):
        self.states.append(deck[:])
        self.player_indices.append(player)

    def copy(self):
        return States(self.states[:], self.player_indices[:])


class GameState:
    def __init__(self, p1, p2, final_p1=None, final_p2=None):
        self.p1 = p1[:]
        self.p2 = p2[:]
        self.final_p1 = final_p1
        self.final_p2 = final_p2

    def key(self):
        return str(p1) + str(p2)

    def __hash__(self):
        return hash(tuple(self.p1)) ^ hash(tuple(self.p2))

    def __eq__(self, other):
        return self.p1 == other.p1 and self.p2 == other.p2


def log(*args):
    # pass
    print(*args)


GAME_COUNTER = 1
PREVIOUS_STATES = set()


def play_recursive_combat(p1, p2):
    global GAME_COUNTER
    global PREVIOUS_STATES

    game = GAME_COUNTER
    GAME_COUNTER += 1

    current_state = GameState(p1, p2)

    if current_state in PREVIOUS_STATES:
        for value in PREVIOUS_STATES:
            if value == current_state:
                return value.final_p1, value.final_p2

    counter = 0
    states = States()

    log(f"=== Game {game} ===")
    log()

    while len(p1) != 0 and len(p2) != 0:

        p1_played = states.lookup_state(p1, 1)
        if p1_played:
            return [0], []
        p2_played = states.lookup_state(p2, 2)
        if p2_played:
            return [0], []

        states.add_state(p1, 1)
        states.add_state(p2, 2)

        counter += 1
        log(f"-- Round {counter} (Game {game})--")
        log(f"Player 1's deck: " + ", ".join(map(str, p1)))
        log(f"Player 2's deck: " + ", ".join(map(str, p2)))
        p1_top = p1.pop(0)
        p2_top = p2.pop(0)
        log(f"Player 1 plays: {p1_top}")
        log(f"Player 2 plays: {p2_top}")

        winner = 0

        if len(p1) >= p1_top and len(p2) >= p2_top:
            log("Playing a sub-game to determine the winner...")
            log()
            new_p1, new_p2 = play_recursive_combat(p1[:p1_top], p2[:p2_top])
            if len(new_p2) == 0:
                winner = 1
            else:
                winner = 2

        else:
            if p1_top > p2_top:
                winner = 1
            else:
                winner = 2

        log(f"Player {winner} wins round {counter} of game {game}!")
        if winner == 1:
            p1.append(p1_top)
            p1.append(p2_top)
        elif winner == 2:
            p2.append(p2_top)
            p2.append(p1_top)
        else:
            raise Exception()

        log()

    log()
    log("== Post-game results ==")
    log(f"Player 1's deck: " + ", ".join(map(str, p1)))
    log(f"Player 2's deck: " + ", ".join(map(str, p2)))

    current_state.final_p1 = p1[:]
    current_state.final_p2 = p2[:]
    PREVIOUS_STATES.add(current_state)
    return p1, p2


def part1():
    p1, p2 = get_decks()
    p1, p2 = play_combat(p1, p2)

    if len(p1) == 0:
        return calculate_score(p2)

    return calculate_score(p1)


def part2():
    p1, p2 = get_decks()
    p1, p2 = play_recursive_combat(p1, p2)

    if len(p1) == 0:
        return calculate_score(p2)

    return calculate_score(p1)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
