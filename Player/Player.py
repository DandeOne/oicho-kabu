class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.cards = []
        self.is_dealer = False

    def change_to_dealer(self):
        self.is_dealer = True

    def change_to_player(self):
        self.is_dealer = False

    def get_cards(self):
        return self.cards

    def add_card(self, card):
        self.cards.append(card)