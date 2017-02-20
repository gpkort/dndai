from Game import Dice


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

