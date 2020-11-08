import unittest
from game import Game
from Player.Player import Player


class TestGame(unittest.TestCase):

    def test_randomize_deck(self):
        test_game = Game()
        test_game.randomize_deck()
        self.assertEqual(len(test_game.deck), 40)

    def test_giving_cards(self):
        test_game = Game()
        a = Player('a', 300)
        b = Player('b', 250)
        c = Player('c', 350)
        d = Player('d', 300)

        test_game.add_players(a, b, c, d)

        test_game.randomize_deck()

        test_game.first_round()

        self.assertEqual(len(a.cards), 1)
        self.assertEqual(len(b.cards), 1)
        self.assertEqual(len(c.cards), 1)
        self.assertEqual(len(d.cards), 1)
        self.assertEqual(len(test_game.deck), 36)


if __name__ == '__main__':
    unittest.main()
