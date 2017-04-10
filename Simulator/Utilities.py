from Game.Characters import PlayerUtilities as pu
from Game.Characters.Fighter import Fighter
from Game.Characters.Monster import Monster
from Game.Characters.Character import Character
from Game.Equipment.Armor import Armor
from Game.Equipment.Weapon import Weapon
from Game.Equipment.Wallet import Wallet
from Game import Dice

GOBLIN_INITIATIVE = 13
NUMBER_OF_FIGHTS = 2
NUMBER_OF_RUNS = 10000


def create_fighter(name: str) -> Fighter:
    fighter = Fighter(name, pu.roll_attributes(3))
    fighter.backpack.weapons.append(Weapon('sword', 20, lambda: Dice.eight_sided(), True))
    fighter.backpack.armors.append(Armor("mail", 10, 5, True))

    return fighter


def make_goblin(gname: str) -> Monster:
    monster = Monster(name=gname, damage=lambda: Dice.eight_sided(), armour=6, xpvalue=6)
    monster.init_hp(6)
    monster.wallet = Wallet(gold=Dice.eight_sided())
    return monster


def fight_to_death(first, second) -> Character:
    firsthit = first.get_hit_roll(second.get_armor_class())
    secondhit = second.get_hit_roll(first.get_armor_class())

    while first.is_alive() and second.is_alive():
        if make_hit(firsthit):
            second.receive_damage(first.get_damage_inflicted())
        if not second.is_alive():
            break
        else:
            if make_hit(secondhit):
                first.receive_damage(second.get_damage_inflicted())

    if not first.is_alive() or not second.is_alive():
        return first if not second.is_alive() else second


def make_hit(roll: int):
    return Dice.twenty_sided() > roll


def fighter_initiative(dexterity) -> bool:
    return Dice.twenty_sided() + pu.BONUS_PENALTIES[dexterity] > GOBLIN_INITIATIVE


def get_results(fighter: Fighter, goblins):
    for gob in goblins:
        if fighter_initiative(fighter.attributes.dexterity):
            fight_to_death(fighter, gob)
        else:
            fight_to_death(gob, fighter)

        if not fighter.is_alive():
            break
        else:
            fighter.add_xp(gob.xp_value)

    att = fighter.attributes
    return att.strength, att.intelligence, att.wisdom, att.dexterity, att.constitution, att.charisma, fighter.get_xp()


def run_battle():
    goblins = []
    fighter = create_fighter("fighter_dude")

    for i in range(0, NUMBER_OF_FIGHTS):
        goblins.append(make_goblin('Goblin' + str(i)))

    print(get_results(fighter, goblins))


if __name__ == '__main__':
    run_battle()
