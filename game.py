import random


def randomize_deck():
    deck = [x for i in range(4) for x in range(1, 11)]
    random.shuffle(deck)
    return deck


def random_dealer_turn(list_of_players):
    random.shuffle(list_of_players)
    return list_of_players


def check_card_sum(player):
    sum_ = player.get_cards().sum()
    return sum_


def give_card(player, card):
    player.add_card(card)


# In first round we give 4 players (not dealer) one card
def first_round(players, deck):
    for player in players:
        card = deck.pop(0)
        player.add_card(card)
