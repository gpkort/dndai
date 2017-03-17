from Game.Equipment import Equipment


class Armor(Equipment):
    def __init__(self, name, weight=0, armor_class: int=0, is_equipped: bool=False):
        Equipment.__init__(self, name, weight)

        assert isinstance(armor_class, float) or isinstance(weight, int)
        assert armor_class is not None

        self.armor_class = armor_class
        self.is_equipped = is_equipped

    def __str__(self):
        return self.get_name()

    def get_name(self) -> object:
        return super().get_name() + ', AC: ' + str(self.armor_class)
