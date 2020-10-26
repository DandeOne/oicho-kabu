import unittest
import game
from Player.Player import Player


class TestGame(unittest.TestCase):

    def test_randomize_deck(self):
        self.assertEqual(len(game.randomize_deck()), 40)

    def test_giving_cards(self):
        a = Player('a', 300)
        b = Player('b', 250)
        c = Player('c', 350)
        d = Player('d', 300)
        deck = game.randomize_deck()
        game.first_round([a, b, c, d], deck)

        self.assertEqual(len(a.get_cards()), 1)
        self.assertEqual(len(b.get_cards()), 1)
        self.assertEqual(len(c.get_cards()), 1)
        self.assertEqual(len(d.get_cards()), 1)
        self.assertEqual(len(deck), 36)


if __name__ == '__main__':
    unittest.main()
