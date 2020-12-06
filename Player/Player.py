from Player.Behaviour import Behaviour


class Player:
    def __init__(self, name, chips, behaviour: Behaviour):
        self._name = name
        self._chips = chips
        self._cards = []
        self._is_dealer = False
        self._behaviour = behaviour

    def __repr__(self):
        return f"(Player {self._name}, chips: {self._chips}, cards: {self._cards}, dealer: {self.is_dealer})"

    def __str__(self):
        return f"(Player {self._name}, chips: {self._chips}, cards: {self._cards}, dealer: {self.is_dealer})"

    @property
    def is_dealer(self):
        return self._is_dealer

    @property
    def name(self):
        return self._name

    def clean_hand(self):
        self._cards = []

    def change_to_dealer(self):
        self._is_dealer = True

    def change_to_player(self):
        self._is_dealer = False

    @property
    def cards(self):
        return self._cards

    @property
    def chips(self):
        return self._chips

    @chips.setter
    def chips(self, value):
        self._chips = value

    def add_card(self, card):
        self._cards.append(card)

    def choose_card(self, cards_and_their_values):
        if self._behaviour is not None:  # Bot
            return self._behaviour.choose_card(cards_and_their_values)
        else:  # Player
            return int(input())

    def decide(self,player, dealer, list_of_players):
        if self._behaviour is not None:  # Bot
            return self._behaviour.decide(player, dealer, list_of_players)
        else:  # Player
            return int(input())

    def bet(self):
        if self._behaviour is not None:  # Bot
            return self._behaviour.bet()
        else:  # Player
            return int(input())
