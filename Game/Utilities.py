"""
Module for general methods needed for game play
"""

from Game import Dice


def roll_attribute_dice(dicard_threshhold=0):
    """
    Attributes are determined by rolling three six sided dice and summing them.
    A original rule allowed for the lowest dice to be re-rolled.
    :param dicard_threshhold: this is to implement re-rolling of lowest dice.
    Since the player would probably would want to keep a the outcome if all dice were high,
    a minimum threshold is allowed and a die is only re-rolled in it is under that threshold

    :return: final sum of three die
    """
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
