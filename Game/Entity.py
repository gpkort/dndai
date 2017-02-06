from abc import ABC, abstractmethod

class Entity(ABC):
    
    def __init__(self, name):
        assert isinstance(name, str)
        self.__name = name

    @abstractmethod
    def get_name(self):
        pass;