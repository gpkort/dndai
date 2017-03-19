import unittest
from Game import Utilities as util, Player as play, PlayerUtilities as pu
from Game.Classes.Fighter import Fighter


class UtilityTests(unittest.TestCase):

    def test_attribute_roll(self):
        roll = util.roll_attribute_dice(3)
        self.assertTrue(3 <= roll < 18)

    def test_roll_attribs(self):
        player = play.Player('Betsy ')
        print('Initial')
        print(player.attributes)

        str0 = player.attributes.strength
        int0 = player.attributes.intelligence
        wis0 = player.attributes.wisdom
        dex0 = player.attributes.dexterity
        con0 = player.attributes.constitution
        chra0 = player.attributes.charisma

        player.attributes = pu.roll_attributes(4)
        print('Second')
        print(player.attributes)

        str1 = player.attributes.strength
        int1 = player.attributes.intelligence
        wis1 = player.attributes.wisdom
        dex1 = player.attributes.dexterity
        con1 = player.attributes.constitution
        chra1 = player.attributes.charisma

        self.assertGreater(str1, str0, "Strength is not set properly")
        self.assertGreater(int1, int0, "Intelligence is not set properly")
        self.assertGreater(wis1, wis0, "Wisdom is not set properly")
        self.assertGreater(dex1, dex0, "Dexterity is not set properly")
        self.assertGreater(con1, con0, "Constitution is not set properly")
        self.assertGreater(chra1, chra0, "Chra is not set properly")




