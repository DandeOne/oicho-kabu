import unittest
from Player.Player import Player


class TestPlayer(unittest.TestCase):
    def test_not_dealer(self):
        john = Player('John', 300)
        self.assertEqual(john.is_dealer, False)

    def test_empty_hand(self):
        john = Player('John', 300)
        self.assertEqual(len(john.cards), 0)


if __name__ == '__main__':
    unittest.main()
