from game import Game


class Behaviour:
    def __init__(self, name, kind):
        self._name = name
        self._type = kind  # One of set {basic bot, bot going for specific combo, mixed bot}

    def __repr__(self):
        return f"(Behaviour {self._name}, {self._kind}"

    def __str__(self):
        return f"(Behaviour {self._name}, {self._kind}"

    def choose_card(self, cards_and_their_values):
        if self._type == 'basic':
            return 0
        if self._type == 'combo':
            # example of cards_and_their_values -> ((0,4),(1,2),(2,5),(3,10))
            index = 0
            for ind, t in cards_and_their_values:
                if t in [10, 1, 4, 9]:
                    index = ind
            return index
        if self._type == 'mixed':
            pass

    def bet(self):
        # For now basic bet, todo
        return 1

    def decide(self, player, dealer, list_of_players):
        if not player.is_dealer:
            return 0 if Game.check_card_sum(player) > Game.check_card_sum(dealer) else 1
        else:
            number_of_probably_wins = 0
            for p in list_of_players:
                if not p.is_dealer and Game.check_card_sum(dealer) > Game.check_card_sum(p):
                    number_of_probably_wins = number_of_probably_wins + 1
            return 0 if number_of_probably_wins > 1 else 1
