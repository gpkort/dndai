from Game import Dice
from Game import Utilities as util
from Game import Player

BONUS_PENALTIES = {3: -3, 4: -2, 5: -2, 6: -1, 7: -1,
                   8: -1, 9: 0,  10: 0, 11: 0, 12: 0,
                   13: 1, 14: 1, 15: 1, 16: 2, 17: 2, 18: 2}


def roll_attributes(player, discard_threshold=0):
    player.strength = util.roll_attribute_dice(discard_threshold)
    player.intelligence = util.roll_attribute_dice(discard_threshold)
    player.wisdom = util.roll_attribute_dice(discard_threshold)
    player.dexterity = util.roll_attribute_dice(discard_threshold)
    player.constitution = util.roll_attribute_dice(discard_threshold)
    player.charisma = util.roll_attribute_dice(discard_threshold)
