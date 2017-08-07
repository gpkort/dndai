"""
Module for Entity class
"""
import uuid


class Entity(object):
    """
    Class that is the base class of all game entities
    """

    def __init__(self, name):
        """
        Constructor of all entities. a unique id is assigned for game tracking purpose
        :param name: All entities should have a name. It is not critical that all entities
        are unique
        """
        assert isinstance(name, str)
        assert name is not None
        self.__name = name
        self.__uuid = str(uuid.uuid4())

    def get_name(self) -> str:
        """
        Accessor for the enitity name
        :return: Entity name
        """
        return self.__name

    def get_unique_id(self) -> str:
        """
        Accessor for entity unique id
        :return: Entity unique id
        """
        return self.__uuid
