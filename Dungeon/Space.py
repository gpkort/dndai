
class Space(object):

    def __init__(self, name: str, width: int, length: int, height: int=0):
        assert name is not None

        assert width is not None
        assert width >= 0

        assert length is not None
        assert length >= 0

        assert height is not None
        assert height >= 0

        self.name = name
        self.width = width
        self.length = length
        self.height = height
