from Game.Equipment import Equipment


class Weapon(Equipment):
    capacity = 100

    def __init__(self, name: str, weight=0, damage=None):
        Equipment.__init__(self, 'Backpack', weight)


