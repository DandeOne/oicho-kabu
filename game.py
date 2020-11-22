import random


class Game:

    def __init__(self):
        self._list_of_players = []
        self._deck = []
        self._table = []
        self._bets = {}

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
        sum_ = sum(player.cards) % 10
        # todo special cards combinations

        return sum_

    # Each player can see his own cards and dealer cards. Other players' second card is always hidden until showdown phase.
    def show_cards(self, person):
        print(f"Showing table for {person}")
        for player in self._list_of_players:
            if (player == person) | player.is_dealer:
                print(f"Player: {player.name}, Dealer: {player.is_dealer}, Cards: {player.cards}")
            else:
                if len(player.cards) == 3:
                    cards = [player.cards[0], player.cards[2]]
                    print(f"Player: {player.name}, Dealer: {player.is_dealer}, Cards: {cards}")
                else:
                    cards = [player.cards[0]]
                    print(f"Player: {player.name}, Dealer: {player.is_dealer}, Cards: {cards}")

        print(f"Table: {self._table}")

    def debug_show_cards(self):
        print(f"Show whole table:")
        for player in self._list_of_players:
            print(f"Player: {player.name}, Dealer: {player.is_dealer}, Cards: {player.cards}")
        print(f"Table: {self._table}")

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
                print(f"{available_cards}")
                choice = int(player.choose_card())
                while choice >= len(available_cards):
                    print(f"Something is wrong with your choice, please try again:")
                    print(f"{available_cards}\n")
                    choice = int(player.choose_card())
                player.add_card(self._table.pop(choice))
                print(f"Set your bet (maximum: {player.chips}):")
                bet = player.bet()
                if (bet <= player.chips) & (bet >= 0):
                    self._bets[player.name] = bet
                else:  # todo better error handling if bet is incorrect
                    print(f"Bet incorrect")

    # In second round each player gets another card and then decides to showdown or draw another card (third one).
    # Remaining card on table gets two cards.
    def second_round(self):
        for player in self.list_of_players:
            if not player.is_dealer:
                player.add_card(self.deck.pop(0))
                self.show_cards(player)
                print("0 - Showdown, 1 - Draw card")
                choice = player.decide()
                if choice:
                    player.add_card(self.deck.pop(0))
                    self.show_cards(player)

        self._table.append(self.deck.pop(0))
        self._table.append(self.deck.pop(0))

        self.get_dealer().add_card(self.deck.pop(0))
        self.show_cards(self.get_dealer())
        print("0 - Showdown, 1 - Draw card")
        choice = self.get_dealer().decide()
        if choice:
            self.get_dealer().add_card(self.deck.pop(0))
            self.show_cards(self.get_dealer())

    def check_results(self):
        dealer = self.get_dealer()
        for player in self.list_of_players:
            if not player.is_dealer:
                print(f"Showdown {dealer.name}: {dealer.cards} vs {player.name}: {player.cards}")
                if self.check_card_sum(dealer) >= self.check_card_sum(player):
                    print(f"Dealer won, bet goes to dealer")
                    dealer.chips = dealer.chips + self.bets[player.name]
                    player.chips = player.chips - self.bets[player.name]
                else:
                    print(f"Player won, bet goes to player")
                    dealer.chips = dealer.chips - self.bets[player.name]
                    player.chips = player.chips + self.bets[player.name]

    def reset_game(self):
        self.randomize_deck()
        self._bets = {}
        self._table = []
