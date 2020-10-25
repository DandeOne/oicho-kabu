# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Player.Player import *
import game


# Press the green button in the gutter to run the script.
john = Player('John', 300)

deck = game.randomize_deck()

print(len(deck))
print(deck)
card = deck.pop(0)
game.give_card(john, card)
print(len(deck))
print(deck)
print(john.get_cards())


