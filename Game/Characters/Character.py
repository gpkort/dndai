"""
Module for Character class
"""
from Game.Entity import Entity
from Game.Equipment.Backpack import Backpack
from Game.Equipment.Wallet import Wallet
from Game.Characters import PlayerUtilities as pu
from Game.Characters.Attributes import Attributes


class Character(Entity):
    """
    This class represents a Character in the game. This could be a player,
    monster or NPC. Character is meant to be abstract
    """

    def __init__(self, name: str, attribs=None):
        super().__init__(name)
        self.__hit_points = 0
        self.__armor_class = 9
        self.__has_hp_set = False
        self.wallet = Wallet()
        self.backpack = Backpack()
        self.attributes = attribs if attribs is not None else Attributes()

    def init_hp(self, hit_points: int):
        """
        Method to allow initialize hit points. Meant ot be called once
        :param hit_points: Initial hit points
        :return: None
        """
        if not self.__has_hp_set:
            self.__hit_points = hit_points
            self.__has_hp_set = True

    def receive_damage(self, hit_points: int) -> int:
        """
        Method when damage is inflicted on character
        :param hit_points: amount of damage
        :return: remaining hit points
        """
        self.__hit_points -= hit_points

        return self.__hit_points

    def get_hit_points(self) -> int:
        """
        Method to retrieve character hit points
        :return: Character hit points
        """
        return self.__hit_points

    def is_alive(self) -> bool:
        """
        method to determine if character is alive based
        on hit points above zero. Character is only alive
        if hit points have been initialized
        :return: hit points above zero
        """
        return self.__has_hp_set and self.__hit_points > 0

    def get_armor_class(self) -> int:
        """
        Overrides base get_armor_class(). factoring characters dexterity
        :return: armor class max is 9
        """
        armorclass = self.backpack.get_armor_class()
        armorclass -= pu.get_armor_class(self.attributes.dexterity)

        armorclass = armorclass if armorclass <= 9 else 9
        return armorclass

    def get_hit_roll(self, armorclass: int) -> int:
        """
        gets the damage inflicted by the character based in targets armor class
        :param armorclass: targets armor class
        :return: dmage inflicted
        """
        return pu.HIT_ROLL_BY_AC[armorclass] - pu.BONUS_PENALTIES[self.attributes.strength]

    def get_damage_inflicted(self, damage=0) -> int:
        """
        Method to determine damage based on weapon
        :param damage: hit roll
        :return: total damage
        """
        damage += self.backpack.get_damage_inflicted()
        return damage
