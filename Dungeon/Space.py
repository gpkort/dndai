
class Space(object):

    def __init__(self, width: int, length: int, height: int=0):
        assert width is not None
        assert width >= 0

        self.widtrh = width