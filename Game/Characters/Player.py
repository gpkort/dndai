"""
Module for Player class
"""
from Game.Characters import PlayerUtilities
from Game.Characters.Character import Character


class Player(Character):
    """
    Class that represents player and non player characters
    """
    def __init__(self, name, attribs=None, xps: int = 0):
        super().__init__(name, attribs)
        self.__experience_points = xps
        self.__level = 0

    def add_xp(self, experience: int = 0) -> int:
        """
        Prefered method to increment experience.  No rule allows experience points to be decremented
        :param experience: to be added to current experience
        :return: New experience value
        """
        self.__experience_points += experience

        return self.__experience_points

    def set_xp(self, experience: int = 0) -> int:
        """
        Method to set experience.  No rule allows experience points to be decremented
        :param experience: to be added to current experience
        :return: New experience value
        """
        self.__experience_points = experience

        return self.__experience_points

    def get_xp(self) -> int:
        """
        Method to get experience.
        :return: Current experience value
        """
        return self.__experience_points

    def get_level(self) -> int:
        """
        Needs to overridden in child classes
        :return:
        """
        pass

    def get_title(self):
        """
        Needs to overridden in child classes
        :return:
        """
        pass

    def get_saving_throw(self, versus_attack)->bool:
        """
        Needs to overridden in child classes
        :return:
        """
        pass

    def get_initial_hit_points(self):
        """
        Needs to overridden in child classes
        :return:
        """
        pass

    def get_armor_class(self) -> int:
        """
        Retrieves the armor rating of a character based on equipped armor
        The lower the better
        :return: the armor class, max armor is nine
        """
        armor_class = PlayerUtilities.get_armor_class(self.attributes.dexterity)

        armor_class += self.backpack.get_armor_class()
        armor_class = armor_class if armor_class <= 9 else 9
        return armor_class

    def get_damage_inflicted(self, damage=0) -> int:
        """
        Retrieves the armor rating of a character based on equipped armor
        The lower the better
        :return: the armor class, max armor is nine
        """
        damage += self.backpack.get_damage_inflicted()
        return damage

    def get_name(self):
        """
        Retieves character name
        :return: base class value with a title of None
        """
        return super().get_name() + ' - None'
