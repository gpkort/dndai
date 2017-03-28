class Attributes(object):
    def __init__(self, strength: int = 3, intell: int = 3, wisdom: int = 3, dex: int = 3, con: int = 3,
                 charisma: int = 3):
        self.strength = strength
        self.intelligence = intell
        self.wisdom = wisdom
        self.dexterity = dex
        self.constitution = con
        self.charisma = charisma

    def __str__(self):
        return str.format('Strength: {}, Intelligence: {}, Wisdom: {}, Dexterity:{}, Constitution: {}, Charisma: {}',
                          self.strength, self.intelligence, self.wisdom, self.dexterity, self.constitution,
                          self.charisma)
