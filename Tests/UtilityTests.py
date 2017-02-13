import unittest
from Game import Utilities

class UtilityTests(unittest.TestCase):

    def test_attribute_roll(self):
        roll = Utilities.roll_atttribute(3)
        self.assertTrue(roll >= 3 and roll < 18 )