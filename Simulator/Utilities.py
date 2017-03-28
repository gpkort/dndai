from Game.Characters import PlayerUtilities as pu
from Game.Characters.Fighter import Fighter
from Game.Characters.Player import Player
from Game.Equipment.Armor import Armor
from Game.Equipment.Weapon import Weapon


def create_fighter(name: str) -> Player:
    player = Player(name, pu.roll_attributes(3))
    player.player_class = Fighter()
    player.backpack.weapons.append(Weapon('sword', 20, lambda: Dice.eight_sided(), True))
    player.backpack.armors.append(Armor("mail", 10, 5, True))
