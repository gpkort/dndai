from Game.Entity import Entity
from Game.Backpack import Backpack


class Attributes(object):
    def __init__(self, strength: int = 0, intell: int = 0, wisdom: int = 0, dex: int = 0, con: int = 0,
                 charisma: int = 0):
        self.strength = strength
        self.intelligence = intell
        self.wisdom = wisdom
        self.dexterity = dex
        self.constitution = con
        self.charisma = charisma

    def __str__(self):
        return str.format('Strength: {}, Intelligence: {}, Wisdom: {}, Dexterity:{}, Constitution: {}, Charisma: {}',
                          self.strength, self.intelligence, self.wisdom, self.dexterity, self.constitution,
                          self.charisma)


class Player(Entity):
    def __init__(self, name):
        Entity.__init__(self, name)

        self.attributes = Attributes()
        self.level = 1
        self.hit_points = 0
        self.armor_class = 0
        self.player_class = None
        self.experience_points = 0
        self.wallet = None
        self.equipment = None
        self.backpack = Backpack()

    def __str__(self):
        return self.get_name() + ' Level: ' + self.level

    def get_armor_class(self):
        pass

    def get_name(self):
        class_name = 'NONE' if self.player_class is None else self.player_class.name
        class_title = '' if self.player_class is None else self.player_class.get_title()

        return super().get_name() + ' - ' + class_name + ', ' + class_title

