from Game import Utilities as util
from Game.Attributes import Attributes
from Game.Player import Player
from Game.Armor import Armor
from Game.Weapon import Weapon
from Game.Classes.Fighter import Fighter
from Game import Dice

BONUS_PENALTIES = {3: -3, 4: -2, 5: -2, 6: -1, 7: -1,
                   8: -1, 9: 0, 10: 0, 11: 0, 12: 0,
                   13: 1, 14: 1, 15: 1, 16: 2, 17: 2, 18: 2}

HIT_ROLL_BY_AC = {9: 10, 8: 11, 7: 12, 6: 13, 5: 14, 4: 15, 3: 16, 2: 17, 1: 18, 0: 19, -1: 20}


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


def create_fighter(name: str) -> Player:
    player = Player(name, roll_attributes(3))
    player.player_class = Fighter()
    player.backpack.weapons.append(Weapon('sword', 20, lambda: Dice.eight_sided(), True))
    player.backpack.armors.append(Armor("mail", 10, 5, True))
