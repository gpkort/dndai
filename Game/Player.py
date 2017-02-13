from Game.Entity import Entity


class Player(Entity):

    def __init__(self, name):
        # assert isinstance(name, str)
        Entity.__init__(self, name)

        self.strength = 0
        self.intelligence = 0
        self.wisdom = 0
        self.dexterity = 0
        self.constitution = 0
        self.charisma = 0
        self.level = 1
        self.hit_points = 0
        self.armor_class = 0
        self.job_class = None
        self.experience_points = 0
        self.wallet = None
        self.equipment = None

    def __str__(self):
        return self.get_name() + ' Level: ' + self.level

    def get_name(self):
        class_name = 'NONE' if self.job_class is None else self.job_class.name
        class_title = '' if self.job_class is None else self.job_class.title

        return self._name + ' - ' + class_name + ', ' + class_title

