from Game.Entity import Entity
from Game.Equipment import Equipment


class Backpack(Entity):

    capacity = 100

    def __init__(self):
        Entity.__init__(self, 'Backpack')

        self.__items = {}
        self.__id = 0

    def get_weight(self):
        weight = 0

        for i in self.__items:
            weight += i.weight

        return weight

    def add_item(self, item: Equipment):
        if self.get_weight() + item <= Backpack.capacity:
            self.__id += 1
            self.__items.


