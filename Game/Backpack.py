from Game.Entity import Entity


class Backpack(Entity):

    capacity = 100

    def __init__(self):
        Entity.__init__(self, 'Backpack')

        self.items = []

