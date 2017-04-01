import unittest
from Game.Characters import PlayerUtilities as pu
from Game.Characters.Player import Player
from Game.Characters.Fighter import Fighter


class FighterTest(unittest.TestCase):
    def test_get(self):
        player = Player('Betsy ')
        player.attributes = pu.roll_attributes(4)
        fighter = Fighter.get_fighter(player)

        self.assertTrue(player.attributes.equals(fighter.attributes))
