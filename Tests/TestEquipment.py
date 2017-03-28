import unittest
from Game import Dice
from Game.Equipment.Equipment import Equipment
from Game.Equipment.Armor import Armor
from Game.Equipment.Backpack import Backpack
from Game.Equipment.Weapon import Weapon


class TestEquipment(unittest.TestCase):
    def test_equipment(self):
        equip = Equipment('test', 20)
        self.assertIsNotNone(equip)

    def test_weapon(self):
        weapon = Weapon('sword', 20, lambda: Dice.eight_sided())
        self.assertIsNotNone(weapon)

    def test_backpack(self):
        bp = Backpack()
        self.assertIsNotNone(bp)

        bp.add_item(Equipment('test1', 10))
        bp.add_item(Equipment('test2', 10))

        self.assertEqual(20, bp.get_weight(), 'Get weight is not equal')
        self.assertEqual(-1, bp.add_item(Equipment('test3', 100)))

    def test_backpack(self):
        bp = Backpack()

        bp.add_item(Equipment('test1', 10))
        eq2 = bp.add_item(Equipment('test2', 10))

        self.assertEqual(20, bp.get_weight(), 'Get weight is not equal')
        bp.pop_item(eq2)
        self.assertEqual(10, bp.get_weight(), 'Get weight is not equal')

    def test_Armor(self):
        bp = Backpack()
        bp.armors.append(Armor("mail", 10, 5, True))
        bp.armors.append(Armor("Platemail", 10, 3, False))
        bp.armors.append(Armor('shield', 30, -2, True))

        self.assertEqual(3, bp.get_armor_class(), "AC is not correct")

    def test_Armor(self):
        bp = Backpack()
        bp.armors.append(Armor("mail", 10, 5, True))
        bp.armors.append(Armor("Platemail", 10, 3, False))
        bp.armors.append(Armor('shield', 30, -2, True))

        self.assertEqual(3, bp.get_armor_class(), "AC is not correct")
