from Game.Entity import Entity
from Game.Backpack import Backpack
from Game import PlayerUtilities
from Game.Attributes import Attributes


class Player(Entity):
    def __init__(self, name, attribs=None, player_class=None):
        Entity.__init__(self, name)

        self.attributes = attribs if attribs is not None else Attributes()
        self.level = 1
        self.hit_points = 0
        self.armor_class = 0
        self.player_class = player_class
        self.experience_points = 0
        self.wallet = None
        self.equipment = None
        self.backpack = Backpack()

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

