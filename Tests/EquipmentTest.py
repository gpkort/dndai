import unittest
from Game.Equipment import Equipment
from Game.Backpack import Backpack
from Game.Weapon import Weapon
from Game import Dice


class EquipmentTests(unittest.TestCase):

    def test_equipment(self):
        equip = Equipment('test', 20)
        print('Equip:')
        print(equip)
        self.assertIsNotNone(equip)

    def test_weapon(self):
        weapon = Weapon('sword', 20, lambda: Dice.eight_sided())
        print('Equip:')
        print(weapon)
        print(weapon.damage())
        print(weapon.damage())
        print(weapon.damage())
        print(weapon.damage())
        self.assertIsNotNone(weapon)

    def test_backpack(self):
        bp = Backpack()
        self.assertIsNotNone(bp)
        print(bp)

        eq1 = bp.add_item(Equipment('test1', 10))
        eq2 = bp.add_item(Equipment('test2', 10))

        self.assertEqual(20, bp.get_weight(), 'Get weight is not equal')
        self.assertEqual(-1, bp.add_item(Equipment('test3', 100)))



