import unittest
from Game.Equipment import Equipment
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

