from Player.Player import *
import game


john = Player('John', 300)
adam = Player('Adam', 250)
miosh = Player('Miosh', 350)
steve = Player('Steve', 300)
dinosaur = Player('T-Rex', 250)

deck = game.randomize_deck()

list_of_players = [john, adam, miosh, steve, dinosaur]
print(list_of_players)
list_of_players = game.random_dealer_turn(list_of_players)
print(list_of_players)

dealer = list_of_players.pop(0)

print(dealer)
print(list_of_players)



