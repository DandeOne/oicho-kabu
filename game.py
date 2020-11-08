import random


class Game:

    def __init__(self):
        self._list_of_players = []
        self._deck = []
        self._table = []
        self._bets = []

    def add_player(self, player):
        self._list_of_players.append(player)

    def add_players(self, *players):
        self._list_of_players.extend(players)

    def randomize_deck(self):
        self._deck = [x for i in range(4) for x in range(1, 11)]
        random.shuffle(self._deck)

    @property
    def deck(self):
        return self._deck

    @property
    def bets(self):
        return self._bets

    @property
    def table(self):
        return self._table

    @property
    def list_of_players(self):
        return self._list_of_players

    def get_dealer(self):
        for player in self._list_of_players:
            if player.is_dealer:
                dealer = player
        return dealer

    def randomize_players_order(self):
        random.shuffle(self._list_of_players)

    def decide_dealer(self):
        self._list_of_players[0].change_to_dealer()

    @staticmethod
    def check_card_sum(player):
        sum_ = (player.get_cards().sum()) % 10
        # todo special cards combinations

        return sum_

    def give_card(self, player):
        card = self._deck.pop(0)
        player.add_card(card)

    # In first round we deal 4 cards on the table
    def first_round(self):
        for i in range(4):
            self._table.append(self._deck.pop(0))

        for player in self._list_of_players:
            if not player.is_dealer:
                print(self._table)
                print(f"Player {player.name}, choose your starting card")
                available_cards = [x for x in range(len(self._table))]
                choice = int(input(f"{available_cards}\n"))
                player.add_card(self._table.pop(choice))
                bet = int(input(f"Set your bet (maximum: {player.chips}): \n"))
                if (bet <= player.chips) & (bet >= 0):
                    self._bets.append((player, bet))
                else:  # todo better error handling if bet is incorrect
                    print(f"Bet incorrect")
