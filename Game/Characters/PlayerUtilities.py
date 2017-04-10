from Game import Utilities as util
from Game.Characters.Attributes import Attributes
from enum import Enum


BONUS_PENALTIES = {3: -3, 4: -2, 5: -2, 6: -1, 7: -1,
                   8: -1, 9: 0, 10: 0, 11: 0, 12: 0,
                   13: 1, 14: 1, 15: 1, 16: 2, 17: 2, 18: 2}

HIT_ROLL_BY_AC = {9: 10, 8: 11, 7: 12, 6: 13, 5: 14, 4: 15, 3: 16, 2: 17, 1: 18, 0: 19, -1: 20}

ABILITY_SCORE_LOOKUP = {
    3: -0.2, 4: -0.2, 5: -0.2,
    6: -0.1, 7: -0.1, 8: -0.1,
    9: 0, 10: 0, 11: 12, 13: 0.05,
    14: 0.05, 15: 0.05, 16: 0.1, 17: 0.1, 18: 0.1
}

class ATTACK_TYPES(Enum):
    DEATH_RAY_POISON = 0,
    MAGIC_WANDS = 1,
    PARALYSIS_STONE = 2,
    DRAGON_BREATH = 3,
    RODS_STAFF_SPELLS = 4


def roll_attributes(discard_threshold=0) -> Attributes:
    return Attributes(util.roll_attribute_dice(discard_threshold),
                      util.roll_attribute_dice(discard_threshold),
                      util.roll_attribute_dice(discard_threshold),
                      util.roll_attribute_dice(discard_threshold),
                      util.roll_attribute_dice(discard_threshold),
                      util.roll_attribute_dice(discard_threshold))


def roll_money() -> int:
    return util.roll_attribute_dice() * 10


def get_armor_class(dexterity: int) -> int:
    ac = BONUS_PENALTIES[dexterity]
    ac = ac * -1 if ac is not None else 0
    return ac



