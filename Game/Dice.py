"""
Module to simulate different dice roll
"""
from random import randrange


def six_sided():
    """
    Simulates the roll of a six sided dice
    :return: outcome of the roll of a six sided die
    """
    return randrange(1, 7)


def four_sided():
    """
        Simulates the roll of a four sided dice
        :return: outcome of the roll of a four sided die
        """
    return randrange(1, 5)


def eight_sided():
    """
        Simulates the roll of an eight sided dice
        :return: outcome of the roll of an eight sided die
        """
    return randrange(1, 9)


def ten_sided():
    """
        Simulates the roll of a ten sided dice
        :return: outcome of the roll of a ten sided die
        """
    return randrange(1, 11)


def twenty_sided():
    """
        Simulates the roll of a twenty sided dice
        :return: outcome of the roll of a twenty sided die
        """
    return randrange(1, 21)
