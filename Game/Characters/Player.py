from Game.Characters import PlayerUtilities
from Game.Characters.Attributes import Attributes
from Game.Characters.Character import Character


class Player(Character):

    def __init__(self, name, attribs=None, player_class=None):
        super().__init__(name)
        self.attributes = attribs if attribs is not None else Attributes()

    def __str__(self):
        return super().get_name()


