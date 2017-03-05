from Game.Entity import Entity


class Equipment(Entity):
    def __init__(self, name: str, weight: object = 0) -> object:
        Entity.__init__(self, name)

        assert weight is not None
        assert isinstance(weight, float) or isinstance(weight, int)

        self.weight = float(weight)

    def __str__(self) -> str:
        return self.get_name()

    def get_name(self) -> str:
        return super().get_name() + ' , Wgt: ' + str(self.weight)
