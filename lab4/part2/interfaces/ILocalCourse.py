from abc import ABC, abstractmethod
from lab4.part2.interfaces.ICourse import ICourse


class ILocalCourse(ICourse, ABC):
    """ Interface to represent LocalCourse"""
    @property
    @abstractmethod
    def lab_number(self):
        """Lab_number property"""
        pass

    @lab_number.setter
    @abstractmethod
    def lab_number(self, value):
        """Lab_number setter"""
        pass

    @abstractmethod
    def insert_into_db(self):
        """Inserts instance into database"""
        pass
