from Game import Dice
from Game.Characters.Player import Player
from Game.Characters import PlayerUtilities as pu


class Fighter(Player):
    SAVING_THROWS = {
        pu.ATTACK_TYPES.DEATH_RAY_POISON: 12,
        pu.ATTACK_TYPES.MAGIC_WANDS: 13,
        pu.ATTACK_TYPES.PARALYSIS_STONE: 14,
        pu.ATTACK_TYPES.DRAGON_BREATH: 15,
        pu.ATTACK_TYPES.RODS_STAFF_SPELLS: 16
    }

    LEVEL_TITLE = {1: "Veteran", 2: "Warrior", 3: "Swordmaster"}
    LEVEL_XP = [[0, 1999], [2000, 3999], [4000, 5999]]

    @staticmethod
    def get_fighter(char: Player):
        fighter = Fighter(char.get_name(), char.attributes)
        fighter.wallet = char.wallet
        fighter.backpack = char.backpack

        return fighter

    def __init__(self, name, attribs=None, xps: int = 0):
        super().__init__(name, attribs, xps)
        self.__experience_points = xps
        self.__level = 0
        self.init_hp(self.get_initial_hit_points())

    def get_saving_throw(self, versus_attack)->bool:
        roll = Dice.twenty_sided()
        return (roll >= Fighter.SAVING_THROWS[versus_attack]), roll

    def get_initial_hit_points(self):
        bonus = pu.BONUS_PENALTIES[self.attributes.constitution]
        bonus = bonus if bonus > 0 else 0
        return Dice.eight_sided() + bonus

    def get_level(self) -> int:
        for idx, level in Fighter.LEVEL_XP:
            if level[1] >= self.__experience_points <= level[2]:
                break
        return idx

    def get_hit_roll(self, ac: int)->int:
        roll = super().get_hit_roll(ac)
        roll -= pu.BONUS_PENALTIES[self.attributes.strength]
        return roll

    def get_damage_inflicted(self, damage: int=0) -> int:
        damage += pu.BONUS_PENALTIES[self.attributes.strength]
        return super().get_damage_inflicted(damage)

    def add_xp(self, xp: float = 0.0):
        bonus = 0 if self.attributes.strength < 13 else (xp * pu.ABILITY_SCORE_LOOKUP[self.attributes.strength])
        total = self.__experience_points + xp + bonus
        super().add_xp(total if total <= Fighter.LEVEL_XP[2][1] else Fighter.LEVEL_XP[2][1])

    def set_xp(self, xp: int = 0):
        super().set_xp(xp if xp <= Fighter.LEVEL_XP[2][1] else Fighter.LEVEL_XP[2][1])

    def get_title(self) -> str:
        return Fighter.LEVEL_TITLE[self.get_level()]
