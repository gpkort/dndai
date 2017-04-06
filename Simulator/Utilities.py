from Game.Characters import PlayerUtilities as pu
from Game.Characters.Fighter import Fighter
from Game.Characters.Monster import Monster
from Game.Characters.Character import Character
from Game.Equipment.Armor import Armor
from Game.Equipment.Weapon import Weapon
from Game import Dice


def create_fighter(name: str) -> Fighter:
    fighter = Fighter(name, pu.roll_attributes(3))
    fighter.backpack.weapons.append(Weapon('sword', 20, lambda: Dice.eight_sided(), True))
    fighter.backpack.armors.append(Armor("mail", 10, 5, True))

    return fighter


def make_goblin(gname: str) -> Monster:
    monster = Monster(name=gname, damage=lambda: Dice.eight_sided(), armour=6, xpval=6)
    monster.init_hp(Dice.six_sided())


def fight_to_death(first, second) -> Character:
    firstHit = first.get_hit_roll(second.get_armor_class())
    secondHit = second.get_hit_roll(first.get_hit_roll())

    while first.is_alive() and second.is_alive():
        if make_hit(firstHit):
            second.receive_damage(first.get_damage_inflicted())
        if second.is_alive():
            break
        else:
            if make_hit(secondHit):
                first.receive_damage(second.get_damage_inflicted())

    if (not first.is_alive() or not second.is_alive()):
        return first if not second.is_alive() else second


def make_hit(roll: int):
    return Dice.twenty_sided() > roll

# if __name__ == '__main__':
#     obj = MyClass()
