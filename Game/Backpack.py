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

    def get_weight(self) -> int:
        weight = 0

        for key in self.__items:
            weight += self.__items[key].weight

        return weight

    def __str__(self) -> str:
        return self.get_name()

    def get_name(self) -> str:
        return super().get_name() + ' , Capacity: ' + str(Backpack.capacity)

    def add_item(self, item: Equipment) -> int:
        if self.get_weight() + item.weight <= Backpack.capacity:
            self.__id += 1
            self.__items.update({self.__id: item})
            return self.__id
        else:
            return -1

    def pop_item(self, id: int) -> Equipment:
        return self.__items.pop(id)

    def get_items(self) -> dict:
        return self.__items.copy()

    def get_armor_class(self) -> int:
        ac = 0
        for a in self.armors:
            if a.is_equipped:
                ac += a.armor_class

        return ac if ac <=9 else 9

    def get_damage_inflicted(self) -> int:
        di = 0
        for w in self.weapons:
            if w.is_armed:
                di += w.get_damage()

        return di
