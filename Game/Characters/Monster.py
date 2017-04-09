from Game.Characters.Character import Character
from Game.Characters.Attributes import Attributes


class Monster(Character):

    def __init__(self, name: str, attribs: Attributes=None, damage=None, armour: int=9, xpvalue: int= 0, spells=None,
                 specials=None):
        """

        :type spells: object
        """
        super().__init__(name, attribs)

        self.damage = damage
        self.armour = armour
        self.spells = spells if spells is not None else []
        self.specials = spells if specials is not None else []
        self.xpvalue = xpvalue

    def get_damage_inflicted(self) -> int:
        return self.damage() if self.damage is not None else super().get_damage_inflicted()

    def get_armor_class(self):
        return self.armour




"""
Armor Class: 6
Hit Dice: 1-1
Move: 90'
Attacks: 1 weapon
Damage: by weapon
No. Appearing: 2-8 (6-60)
Save As: Normal man
Morale: 7 or 9
Treasure Type: (r) c
Alignment: chaotic
XP value: 5

"""
