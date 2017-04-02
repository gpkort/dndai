from Game.Characters import PlayerUtilities as pu
from Game.Characters.Fighter import Fighter
from Game.Characters.Monster import Monster
from Game.Equipment.Armor import Armor
from Game.Equipment.Weapon import Weapon
from Game import Dice


def create_fighter(name: str) -> Fighter:
    fighter = Fighter(name, pu.roll_attributes(3))
    fighter.backpack.weapons.append(Weapon('sword', 20, lambda: Dice.eight_sided(), True))
    fighter.backpack.armors.append(Armor("mail", 10, 5, True))

    return fighter


def make_goblin(gname: str) -> Monster:
    monster = Monster(name=gname, damage=lambda: Dice.eight_sided(), armour=6)
    monster.init_hp(Dice.six_sided())

def make_fight(combatants:list):
    assert len(combatants) == 2




# if __name__ == '__main__':
#     obj = MyClass()
