from Game import Dice
from Game import Utilities as util
from Game import Player


def roll_attributes(player, discard_threshhold=0):
    player.strength = util.roll_attribute_dice(discard_threshhold)
    player.intelligence = util.roll_attribute_dice(discard_threshhold)
    player.wisdom = util.roll_attribute_dice(discard_threshhold)
    player.dexterity = util.roll_attribute_dice(discard_threshhold)
    player.constitution = util.roll_attribute_dice(discard_threshhold)
    player.charisma = util.roll_attribute_dice(discard_threshhold)
