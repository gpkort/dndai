import unittest
from Game.Characters import PlayerUtilities as pu
from Game.Characters.Player import Player
from Game.Characters.Fighter import Fighter


class FighterTest(unittest.TestCase):

    def test_get(self):
        player = Player('Betsy ')

        str0 = player.attributes.strength
        int0 = player.attributes.intelligence
        wis0 = player.attributes.wisdom
        dex0 = player.attributes.dexterity
        con0 = player.attributes.constitution
        chra0 = player.attributes.charisma

        player.attributes = pu.roll_attributes(4)

        fighter = Fighter.get_fighter(player)

        self.assertTrue(player.attributes.equals(fighter.attributes))


