import unittest
import Simulator.Utilities as su
import Game.Characters.PlayerUtilities as pu


class UtilityTests(unittest.TestCase):
    def test_make_goblin(self):
        gob = su.make_goblin('Gob1')
        self.assertEqual(gob.xpvalue, 6, 'xp is not correct')
        dam = gob.get_damage_inflicted()
        self.assertTrue(0 < dam < 9, 'dice roll is wrong')
        self.assertTrue(0 < gob.get_hit_points() < 7, 'HP is wrong')

    def test_attack(self):
        fight = su.create_fighter('test1')
        gob = su.make_goblin('Gob1')
        strength = fight.attributes.strength
        bonus = pu.BONUS_PENALTIES[strength]
        roll = 13

        hr = fight.get_hit_roll(gob.get_armor_class())
        self.assertEqual(roll-bonus, hr, 'Hit roll is off')
        print('hr = ' + str(hr))

    def test_defense(self):
        fight = su.create_fighter('test1')
        fac = 5 - pu.BONUS_PENALTIES[fight.attributes.dexterity]
        self.assertEqual(fac, fight.get_armor_class(), 'fighter ac is wrong')
        print('FAC = {}'.format(fac))
