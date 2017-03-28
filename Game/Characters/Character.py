from Game.Entity import Entity
from Game.Equipment.Backpack import Backpack


class Character(Entity):
    def __init__(self, name: str):
        super().__init__(name)
        self.__hit_points = 0
        self.__armor_class = 9
        self.__has_hp_set = False
        self.wallet = None
        self.backpack = Backpack()

    def init_hp(self, hit_points: int):
        if self.__has_hp_set:
            self.__hit_points = hit_points
            self.__has_hp_set = True

    def receive_damage(self, hit_points: int):
        self.__hit_points -= hit_points

    def is_alive(self)-> bool:
        return self.__has_hp_set and self.__hit_points > 0

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
