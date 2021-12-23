from abc import ABC, abstractmethod
from lab4.part2.interfaces.ICourse import ICourse


class IOffsiteCourse(ICourse, ABC):
    """ Interface to represent OffsiteCourse"""
    @property
    @abstractmethod
    def place(self):
        """place property"""
        pass

    @place.setter
    @abstractmethod
    def place(self, value):
        """place setter"""
        pass

    @abstractmethod
    def insert_into_db(self):
        """Inserts instance into database"""
        pass
