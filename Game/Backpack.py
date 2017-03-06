from Game.Entity import Entity
from Game.Equipment import Equipment
from Game.Armor import Armor

class Backpack(Entity):

    capacity = 100

    def __init__(self):
        Entity.__init__(self, 'Backpack')

        self.__items = {}
        self.__id = 0
        self.armors = []
        self.weapons = []

    def get_weight(self):
        weight = 0

        for i in self.__items:
            weight += i.weight

        return weight

    def add_item(self, item: Equipment) -> int:
        if self.get_weight() + item <= Backpack.capacity:
            self.__id += 1
            self.__items.update({self.__id:item})
            return self.__id
        else:
            return -1

    def get_items(self) -> dict:
        return self.__items.copy()

    def get_armor_class(self) -> int:
        ac = 9
        for a in self.armors:
            if a.is_equipped:
                ac += a.armor_class

        return ac

    def get_damage_inflicted(self) -> int:
        di = 9
        for w in self.weapons:
            if w.is_equipped:
                di += w.get_damage()

        return di




