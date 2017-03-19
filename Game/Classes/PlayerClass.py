from Game import PlayerUtilities as pu
from Game.Classes import ClassUtilities as cu


class PlayerClass(object):
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


