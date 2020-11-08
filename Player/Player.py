class Player:
    def __init__(self, name, chips):
        self._name = name
        self._chips = chips
        self._cards = []
        self._is_dealer = False

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

    def add_card(self, card):
        self._cards.append(card)
