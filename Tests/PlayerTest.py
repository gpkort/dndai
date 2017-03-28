import unittest

from Game import Dice
from Game.Characters.Player import Player
from Game.Equipment.Equipment import Equipment
from Game.Equipment.Armor import Armor
from Game.Equipment.Weapon import Weapon


class PlayerTests(unittest.TestCase):
    def test_player_fail(self):
        with self.assertRaises(TypeError):
            Player()

    def test_player_fail_type(self):
        with self.assertRaises(AssertionError):
            Player(1)

    def test_player_fail_empty(self):
        with self.assertRaises(AssertionError):
            Player('')

    def test_player_good(self):
        greg = Player('greg')
        self.assertEqual('greg - NONE, ', greg.get_name(), 'Name doesn\'t match')

    def test_Equip_fail_type(self):
        with self.assertRaises(AssertionError):
            Equipment('equip', '1')

    def test_Equip_fail_none(self):
        with self.assertRaises(AssertionError):
            Equipment('equip', None)

    def test_equipment_str(self):
        equip = Equipment('equipment', 10)
        self.assertEqual(str(equip), 'equipment , Wgt: 10')

    def test_Armor_fail_type(self):
        with self.assertRaises(AssertionError):
            Armor('mail', 10.0, '1')

    def test_Armor_fail_none(self):
        with self.assertRaises(AssertionError):
            Armor('equip', 9, None)

    def test_Armor(self):
        play = Player('Greg')
        bp = play.backpack
        bp.armors.append(Armor("mail", 10, 5, True))
        bp.armors.append(Armor("Platemail", 10, 3, False))
        bp.armors.append(Armor('shield', 30, -2, True))

        self.assertEqual(3, bp.get_armor_class(), "AC is not correct")
        play.attributes.dexterity = 18
        self.assertEqual(1, play.get_armor_class(), "AC is not correct")
        play.attributes.dexterity = 3
        self.assertEqual(6, play.get_armor_class(), "AC is not correct")

    def test_Damage(self):
        play = Player('Greg')
        bp = play.backpack
        bp.weapons.append(Weapon('sword', 20, lambda: Dice.eight_sided(), True))
        dam = play.get_damage_inflicted()
        print(str.format("Damage: {}", dam))
        self.assertTrue(1 <= dam <= 8)
