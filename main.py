from Player.Player import *
from game import Game

# Create Players
john = Player('John', 300)
adam = Player('Adam', 250)
miosh = Player('Miosh', 350)
dinosaur = Player('T-Rex', 250)
# Create Game
game = Game()
game.add_players(john, adam, miosh, dinosaur)
game.randomize_deck()

# Deciding order of players and who is first dealer
game.randomize_players_order()
game.decide_dealer()

game.first_round()

game.give_card(game.get_dealer())

game.second_round()

game.debug_show_cards()
# Game loop
# Done
## Decide who is the dealer in this round
## Show 4 cards on the table and give one card to dealer which is also seen to everyone
# Done
## Players in specific order decide which card will be their starting one with bet
## Bets can be different between players.

# Done
## In next round each player gets one card and decides if they are standing (Showdown) or drawing another one (Draw card)
## Some cards are hidden so other players (and dealer) can't determine what is exact sum of cards.
## After that dealer draws card and decides to stand or draw one more

# Todo
## Then dealer compares each player's hand with his. If player wins then amount of his bet is given to him.
## If player loses then bet goes to dealer

# End of Game loop
# Change dealer and order of players and return to game loop

## In Yakuza Kiwami there are 4 players. One is a dealer then the rest chooses their starting hand.
## Remaining card will always have 3 cards in total which are visible to all players.
