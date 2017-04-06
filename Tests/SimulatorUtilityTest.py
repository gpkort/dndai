import unittest

import Simulator.Utilities as su


class UtilityTests(unittest.TestCase):
    def test_make_goblin(self):
        gob = su.make_goblin('Gob1')
        self.assertEqual(gob.xpvalue, 6, 'xp is not correct')




