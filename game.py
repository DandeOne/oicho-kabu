import random


def randomize_deck():
    deck = [x for i in range(4) for x in range(1, 11)]
    random.shuffle(deck)
    return deck


def check_card_sum(player):
    sum = player.get_cards().sum()
    return sum


def give_card(player, card):
    player.add_card(card)
