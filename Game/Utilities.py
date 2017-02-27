from Game import Dice
from enum import Enum


def roll_attribute_dice(dicard_threshhold=0):
    die1 = Dice.six_sided()
    die2 = Dice.six_sided()
    die3 = Dice.six_sided()

    if die1 <= dicard_threshhold:
        die1 = Dice.six_sided()
    elif die2 <= dicard_threshhold:
        die2 = Dice.six_sided()
    elif die3 <= dicard_threshhold:
        die3 = Dice.six_sided()

    return die1 + die2 + die3


class ATTACK_TYPES(Enum):
    DEATH_RAY_POISON = 0,
    MAGIC_WANDS = 1,
    PARALYSIS_STONE = 2,
    DRAGON_BREATH = 3,
    RODS_STAFF_SPELLS = 4
