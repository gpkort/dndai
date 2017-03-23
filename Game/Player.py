from Game.Character import Character
from Game import PlayerUtilities
from Game.Attributes import Attributes


class Player(Character):

    def __init__(self, name, attribs=None, player_class=None):
        super().__init__(name)

        self.attributes = attribs if attribs is not None else Attributes()
        self.level = 1
        self.player_class = player_class
        self.experience_points = 0
        self.equipment = None

    def __str__(self):
        return self.get_name() + ' Level: ' + self.level

    def get_armor_class(self) -> int:
        ac = PlayerUtilities.get_armor_class(self.attributes.dexterity)

        ac += self.backpack.get_armor_class()
        ac = ac if ac <= 9 else 9
        return ac

    def get_damage_inflicted(self) -> int:
        damage = 0
        damage += self.backpack.get_damage_inflicted()
        return damage


    def get_name(self):
        class_name = 'NONE' if self.player_class is None else self.player_class.name
        class_title = '' if self.player_class is None else self.player_class.get_title()

        return super().get_name() + ' - ' + class_name + ', ' + class_title

