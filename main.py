from Player.Player import Player
from Player.Behaviour import Behaviour
from game import Game
import time

number_of_games = 10000
sum_of_wins = [0, 0, 0, 0]
sum_of_loses = [0, 0, 0, 0]
start = time.perf_counter()
for n in range(number_of_games):
    # Create Players
    base_chips = (300, 250, 350, 250)
    john = Player('John', base_chips[0], Behaviour('john_bot', 'basic'))
    adam = Player('Adam', base_chips[1], Behaviour('john_bot', 'basic'))
    miosh = Player('Miosh', base_chips[2], Behaviour('john_bot', 'basic'))
    dinosaur = Player('T-Rex', base_chips[3], Behaviour('john_bot', 'basic'))
    # Create Game
    game = Game()
    game.add_players(john, adam, miosh, dinosaur)
    game.randomize_deck()

    # Deciding order of players and who is first dealer
    game.randomize_players_order()
    game.decide_dealer()
    # print(game.list_of_players)
    game.first_round()

    game.give_card(game.get_dealer())

    game.second_round()

    game.debug_show_cards()

    game.check_results()
    # print(game.list_of_players)
    for ind, player, bet in zip([0, 1, 2, 3], [john, adam, miosh, dinosaur], base_chips):
        if player.chips > bet:
            sum_of_wins[ind] = sum_of_wins[ind] + 1
        else:
            sum_of_loses[ind] = sum_of_loses[ind] + 1
end = time.perf_counter()
print(f"Number of games: {number_of_games}, time: {end - start:0.2f} seconds")
for ind, player in zip(range(4), [john, adam, miosh, dinosaur]):
    print(f"Number of games {player.name} won: {sum_of_wins[ind]}, lost: {sum_of_loses[ind]}")
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
## Then dealer compares each player's hand with his. If player wins then amount of his bet is given to him.
## If player loses then bet goes to dealer
## Behaviour class for computer players to get from them specific actions and make human vs bots games possible
# End of Game loop
# Change dealer and order of players and return to game loop

# Todo
## Implement sum of points in specific combinations of cards in hand
