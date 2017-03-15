from Game.Classes.PlayerClass import PlayerClass
from Game.Classes import ClassUtilities as cu
from Game import Dice, PlayerUtilities as pu


class Fighter(PlayerClass):
    SAVING_THROWS = {
        cu.ATTACK_TYPES.DEATH_RAY_POISON: 12,
        cu.ATTACK_TYPES.MAGIC_WANDS: 13,
        cu.ATTACK_TYPES.PARALYSIS_STONE: 14,
        cu.ATTACK_TYPES.DRAGON_BREATH: 15,
        cu.ATTACK_TYPES.RODS_STAFF_SPELLS: 16
    }

    LEVEL_TITLE = {1: "Veteran", 2: "Warrior", 3: "Swordmaster"}
    LEVEL_XP = [[0,1999], [2000, 3999], [4000, 5999]]

    def get_saving_throw(self, versus_attack):
        roll = Dice.twenty_sided()
        return (roll >= Fighter.SAVING_THROWS[versus_attack]), roll

    def get_initial_hit_points(self):
        return Dice.eight_sided()

    def get_level(self) -> int:
        idx = 0

        for level in Fighter.LEVEL_XP:
            idx += 1
            if level[1] >= self.__experience_points <= level[2]:
                break
        return idx

    def add_xp(self, xp: int = 0):

        total = self.__experience_points + xp
        self.__experience_points = total if total <= Fighter.LEVEL_XP[3][2] else Fighter.LEVEL_XP[3][2]

    def set_xp(self, xp: int = 0):
        self.__experience_points = xp if xp <= Fighter.LEVEL_XP[3][2] else Fighter.LEVEL_XP[3][2]

    def get_title(self)->str:
        return Fighter.LEVEL_TITLE[self.get_level()]

    def get_armor_class(self, dexterity: int) -> int:
        return super().get_armor_class(dexterity)
