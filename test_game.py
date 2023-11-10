import unittest
from game import Game

class TestGame(unittest.TestCase):

    def test_zero_players_game_is_not_allowed(self):
        self.assertRaises(ValueError, Game, 0)

    def test_one_players_game_is_not_allowed(self):
        self.assertRaises(ValueError, Game, 1)

    def test_two_players_game_is_allowed(self):
        game = Game(2)
        self.assertIsNotNone(game)

    def test_three_players_game_is_allowed(self):
        game = Game(3)
        self.assertIsNotNone(game)
    
    def test_four_players_game_is_allowed(self):
        game = Game(4)
        self.assertIsNotNone(game)
    
    def test_five_players_game_is_not_allowed(self):
        self.assertRaises(ValueError, Game, 5)

if __name__ == '__main__':
    unittest.main()