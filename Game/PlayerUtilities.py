from Game import Dice
from Game import Utilities as util
from Game import Player

BONUS_PENALTIES = {3: -3, 4: -2, 5: -2, 6: -1, 7: -1,
                   8: -1, 9: 0, 10: 0, 11: 0, 12: 0,
                   13: 1, 14: 1, 15: 1, 16: 2, 17: 2, 18: 2}

HIT_ROLL_BY_AC = {9: 10, 8: 11, 7: 12, 6: 13, 5: 14, 4: 15, 3: 16, 2: 17, 1: 18, 0: 19, -1: 20}


def roll_attributes(player, discard_threshold=0):
    player.strength = util.roll_attribute_dice(discard_threshold)
    player.intelligence = util.roll_attribute_dice(discard_threshold)
    player.wisdom = util.roll_attribute_dice(discard_threshold)
    player.dexterity = util.roll_attribute_dice(discard_threshold)
    player.constitution = util.roll_attribute_dice(discard_threshold)
    player.charisma = util.roll_attribute_dice(discard_threshold)


def roll_money() -> int:
    return util.roll_attribute_dice() * 10



