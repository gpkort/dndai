from Game.Equipment import Equipment


class Weapon(Equipment):
    capacity = 100

    def __init__(self, name: str, weight, damage):
        Entity.__init__(self, 'Backpack')

        self.items = []