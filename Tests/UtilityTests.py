import unittest
from Game import Utilities as util, Player as play, PlayerUtilities as pu


class UtilityTests(unittest.TestCase):

    def test_attribute_roll(self):
        roll = util.roll_attribute_dice(3)
        self.assertTrue(3 <= roll < 18)

    def test_roll_attribs(self):
        player = play.Player('Betsy ')
        print('Initial')
        player.print_attributes()

        str0 = player.strength
        int0 = player.intelligence
        wis0 = player.wisdom
        dex0 = player.dexterity
        con0 = player.constitution
        chra0 = player.charisma

        pu.roll_attributes(player, 4)
        print('Second')
        player.print_attributes()

        str1 = player.strength
        int1 = player.intelligence
        wis1 = player.wisdom
        dex1 = player.dexterity
        con1 = player.constitution
        chra1 = player.charisma

        self.assertGreater(str1, str0, "Strength is not set properly")
        self.assertGreater(int1, int0, "Intelligence is not set properly")
        self.assertGreater(wis1, wis0, "Wisdom is not set properly")
        self.assertGreater(dex1, dex0, "Dexterity is not set properly")
        self.assertGreater(con1, con0, "Constitution is not set properly")
        self.assertGreater(chra1, chra0, "Chra is not set properly")




