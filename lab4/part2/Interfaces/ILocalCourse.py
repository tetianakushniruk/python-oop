from abc import ABC, abstractmethod
from lab4.part2.Interfaces.ICourse import ICourse


class ILocalCourse(ICourse, ABC):
    @property
    @abstractmethod
    def lab_number(self):
        pass

    @lab_number.setter
    @abstractmethod
    def lab_number(self, value):
        pass

    @abstractmethod
    def insert_into_db(self):
        pass
