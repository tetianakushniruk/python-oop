from abc import ABC, abstractmethod


class ITeacher(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstractmethod
    def surname(self):
        pass

    @surname.setter
    @abstractmethod
    def surname(self, value):
        pass

    @abstractmethod
    def insert_into_db(self):
        pass

    @classmethod
    @abstractmethod
    def get_by_id(cls, id):
        pass

    @abstractmethod
    def del_from_db(self):
        pass

    @abstractmethod
    def get_courses(self):
        pass
