from Game.Characters import PlayerUtilities
from Game.Characters.Character import Character


class Player(Character):
    def __init__(self, name, attribs=None, xps: int = 0):
        super().__init__(name, attribs)
        self.__experience_points = xps
        self.__level = 0

    def add_xp(self, xp: int = 0):
        self.__experience_points += xp

    def set_xp(self, xp: int = 0):
        self.__experience_points = xp

    def get_xp(self) -> int:
        return self.__experience_points

    def get_level(self) -> int:
        pass

    def get_title(self):
        pass

    def get_saving_throw(self, versus_attack)->bool:
        pass

    def get_initial_hit_points(self):
        pass

    def get_armor_class(self) -> int:
        ac = PlayerUtilities.get_armor_class(self.attributes.dexterity)

        ac += self.backpack.get_armor_class()
        ac = ac if ac <= 9 else 9
        return ac

    def get_damage_inflicted(self, damage=0) -> int:
        damage += self.backpack.get_damage_inflicted()
        return damage

    def get_name(self):
        return super().get_name() + ' - None'
