from Game.Entity import Entity
from Game.Equipment.Backpack import Backpack
from Game.Equipment.Wallet import Wallet
from Game.Characters import PlayerUtilities
from Game.Characters.Attributes import Attributes


class Character(Entity):
    def __init__(self, name: str, attribs: Attributes=None):
        super().__init__(name)
        self.__hit_points = 0
        self.__armor_class = 9
        self.__has_hp_set = False
        self.wallet = Wallet()
        self.backpack = Backpack()
        self.attributes = attribs if attribs is not None else Attributes()

    def init_hp(self, hit_points: int):
        if self.__has_hp_set:
            self.__hit_points = hit_points
            self.__has_hp_set = True

    def receive_damage(self, hit_points: int):
        self.__hit_points -= hit_points

    def get_hit_points(self):
        return self.__hit_points

    def is_alive(self)-> bool:
        return self.__has_hp_set and self.__hit_points > 0

    def get_armor_class(self) -> int:
        ac = self.backpack.get_armor_class()
        ac -= PlayerUtilities.get_armor_class(self.attributes.dexterity)

        ac = ac if ac <= 9 else 9
        return ac

    def get_hit_roll(self, ac: int) -> int:
        return PlayerUtilities.HIT_ROLL_BY_AC[ac]

    def get_damage_inflicted(self) -> int:
        damage = 0
        damage += self.backpack.get_damage_inflicted()
        return damage

    def get_name(self):
        return super().get_name()
