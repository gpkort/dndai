from Game.Characters.Player import Player

class PlayerClass(Player):
    def __init__(self, xps: int=0):
        self.__experience_points = xps
        self.__level = 0
        self.__name = ''

    def add_xp(self, xp: int=0):
        self.__experience_points += xp

    def set_xp(self, xp: int=0):
        self.__experience_points = xp

    def get_xp(self)->int:
        return self.__experience_points

    def get_level(self)->int:
        pass

    def get_hit_roll(self)->int:
        pass

    def get_title(self):
        pass

    def get_saving_throw(self, versus_attack):
        pass

    def get_initial_hit_points(self):
        pass

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


