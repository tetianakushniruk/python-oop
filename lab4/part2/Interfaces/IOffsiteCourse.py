from abc import ABC, abstractmethod
from lab4.part2.Interfaces.ICourse import ICourse


class IOffsiteCourse(ICourse, ABC):
    @property
    @abstractmethod
    def place(self):
        pass

    @place.setter
    @abstractmethod
    def place(self, value):
        pass

    @abstractmethod
    def insert_into_db(self):
        pass
