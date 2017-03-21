from Dungeon.Space import Space

class Room(Space):

    def __init__(self, name: str, width: int, length: int, height: int=0):
        super.__init__(name, width, length, height)