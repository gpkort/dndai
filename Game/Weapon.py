from Game.Equipment import Equipment


class Weapon(Equipment):
    capacity = 100

    def __init__(self, name: str, weight: int=0, damage=None, is_armed: bool=False):
        Equipment.__init__(self, name, weight)
        self.damage = damage
        self.is_armed = is_armed

    def get_damage(self):
        points = self.damage() if self.damage is not None else 0
        return points



