import unittest
from Game import Player as pl

class PlayerTests(unittest.TestCase):

    def test_player_fail(self):
        with self.assertRaises(TypeError):
            pl.Player()

    def test_player_fail_type(self):
        with self.assertRaises(TypeError):
            pl.Player(1)

    def test_player_fail_type(self):
        with self.assertRaises(AssertionError):
            pl.Player('')

    def test_player_good(self):
        greg = pl.Player('greg')
        self.assertEqual('greg - NONE, ', greg.get_name(), 'Name doesn\'t match')
