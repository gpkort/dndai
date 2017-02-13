from abc import ABC, abstractmethod

class Entity(object):
    
    def __init__(self, name):
        assert isinstance(name, str)
        assert name is not None
        assert len(name) > 0
        self._name = name

    @abstractmethod
    def get_name(self):
        pass