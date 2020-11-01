from Player.Player import *
import game

# Create Players
john = Player('John', 300)
adam = Player('Adam', 250)
miosh = Player('Miosh', 350)
steve = Player('Steve', 300)
dinosaur = Player('T-Rex', 250)
# Randomizing deck
deck = game.randomize_deck()

# Deciding order of players and who is first dealer
list_of_players = [john, adam, miosh, steve, dinosaur]
print(list_of_players)
list_of_players = game.random_dealer_turn(list_of_players)
print(list_of_players)

dealer = list_of_players.pop(0)

print(dealer)
print(list_of_players)

# Game loop
## Decide who is the dealer in this round
## Show 4 cards on the table and give one card to dealer which is also seen to everyone

## Players in specific order decide which card will be their starting one with bet
## Bets can be different between players.
## In next round each player gets one card and decides if they are standing (Showdown) or drawing another one (Draw card)
## Some cards are hidden so other players (and dealer) can't determine what is exact sum of cards.

## After that dealer draws card and decides to stand or draw one more
## Then dealer compares each player's hand with his. If player wins then amount of his bet is given to him.
## If player loses then bet goes to dealer

# End of Game loop
# Change dealer and order of players and return to game loop

## In Yakuza Kiwami there are 4 players. One is a dealer then the rest chooses their starting hand.
## Remaining card will always have 3 cards in total which are visible to all players.