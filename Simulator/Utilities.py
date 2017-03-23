from Game.Player import Player
from Game.Weapon import Weapon
from Game.Armor import Armor
from Game.Classes.Fighter import Fighter

from Game import PlayerUtilities as pu


def create_fighter(name: str) -> Player:
    player = Player(name, pu.roll_attributes(3))
    player.player_class = Fighter()
    player.backpack.weapons.append(Weapon('sword', 20, lambda: Dice.eight_sided(), True))
    player.backpack.armors.append(Armor("mail", 10, 5, True))
