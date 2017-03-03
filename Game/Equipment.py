from Game.Entity import Entity


class Equipment(Entity):
    def __init__(self, name: str, weight=0):
        Entity.__init__(self, name)

        assert weight is not None
        assert isinstance(weight, float) or isinstance(weight, int)

        self.weight = float(weight)

    def __str__(self) -> object:
        return self.get_name()

    def get_name(self):
        return super().get_name() + ' , Wgt: ' + str(self.weight)
