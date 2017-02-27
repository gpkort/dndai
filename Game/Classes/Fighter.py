from Game.Classes import PlayerClass
from Game import Dice, Utilities as ut


class Fighter(PlayerClass):
    SAVING_THROWS = {
        ut.ATTACK_TYPES.DEATH_RAY_POISON: 12,
        ut.ATTACK_TYPES.MAGIC_WANDS: 13,
        ut.ATTACK_TYPES.PARALYSIS_STONE: 14,
        ut.ATTACK_TYPES.DRAGON_BREATH: 15,
        ut.ATTACK_TYPES.RODS_STAFF_SPELLS: 16
    }

    def get_hit_roll(self) -> float:
        return float(Dice.eight_sided())

    def get_saving_throw(self, versus_attack: ut.ATTACK_TYPES) -> list[:bool, :float]:
        roll = Dice.twenty_sided()
        return [(roll >= Fighter.SAVING_THROWS[versus_attack]), roll]
