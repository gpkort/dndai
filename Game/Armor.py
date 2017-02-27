from Game.Equipment import Equipment


class Armor(Equipment):
    def __init__(self, name, weight=0, armorclass=0):
        Equipment.__init__(self, name, weight)

        assert isinstance(armorclass, float) or isinstance(weight, int)
        assert armorclass is not None

        self.armorclass = float(armorclass)

    def __str__(self):
        return self.get_name()

    def get_name(self) -> object:
        return super().get_name() + ', Wgt: ' + str(self.weight) + ', AC: ' + str(self.armorclass)
