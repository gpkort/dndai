import unittest
from Game import Player as pl, Equipment as eq, Armor as ar

class PlayerTests(unittest.TestCase):

    def test_player_fail(self):
        with self.assertRaises(TypeError):
            pl.Player()

    def test_player_fail_type(self):
        with self.assertRaises(AssertionError):
            pl.Player(1)

    def test_player_fail_empty(self):
        with self.assertRaises(AssertionError):
            pl.Player('')

    def test_player_good(self):
        greg = pl.Player('greg')
        self.assertEqual('greg - NONE, ', greg.get_name(), 'Name doesn\'t match')

    def test_Equip_fail_type(self):
        with self.assertRaises(AssertionError):
            eq.Equipment('equip', '1')

    def test_Equip_fail_none(self):
        with self.assertRaises(AssertionError):
            eq.Equipment('equip', None)

    def test_equipment_str(self):
        equip = eq.Equipment('equipment', 10)
        self.assertEqual(str(equip), 'equipment , Wgt: 10.0')

    def test_Armor_fail_type(self):
        with self.assertRaises(AssertionError):
            ar.Armor('mail', 10.0, '1')

    def test_Armor_fail_none(self):
        with self.assertRaises(AssertionError):
            ar.Armor('equip', 9, None)

    def test_Armor_str(self):
        armor = ar.Armor('equipment', 10, 3.5)
        self.assertEqual(str(armor), 'equipment, Wgt: 10.0, AC: 3.5')
