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

    def reallocate(self, source: str, target: str):
        sourceval = self.get_attribute(source.upper())
        targetval = self.get_attribute(target.upper())

        if sourceval > 4 and 3 <= targetval <= 16:
            self.set_attribute(source, sourceval - 2)
            self.set_attribute(target, targetval + 2)

    def set_attribute(self, name: str, value: int):
        if name.upper() == 'STRENGTH':
            self.strength = value
        elif name.upper() == 'INTELLIGENCE':
            self.intelligence = value
        elif name.upper() == 'WISDOM':
            self.wisdom = value
        elif name.upper() == 'DEXTERITY':
            self.dexterity = value
        elif name.upper() == 'CONSTITUTION':
            self.constitution = value
        elif name.upper() == 'CHARISMA':
            self.charisma = value

    def get_attribute(self, name: str) -> int:
        return {
            'STRENGTH': self.strength,
            'INTELLIGENCE': self.intelligence,
            'WISDOM': self.wisdom,
            'DEXTERITY': self.dexterity,
            'CONSTITUTION': self.constitution,
            'CHARISMA': self.charisma
        }.get(name, -1)

    def equals(self, attribs) -> bool:
        """

        :type attribs: Attributes
        """
        if type(attribs) is self:
            return True

        if type(attribs) is not Attributes:
            return False

        return self.strength == attribs.strength \
               and self.intelligence == attribs.intelligence \
               and self.wisdom == attribs.wisdom \
               and self.dexterity == attribs.dexterity \
               and self.constitution == attribs.constitution \
               and self.charisma == attribs.charisma
