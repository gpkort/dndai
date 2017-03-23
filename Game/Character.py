from Game.Entity import Entity
from Game.Backpack import Backpack


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
