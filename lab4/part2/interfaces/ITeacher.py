from abc import ABC, abstractmethod


class ITeacher(ABC):
    """ Interface to represent Teacher"""
    @property
    @abstractmethod
    def name(self):
        """name property"""
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        """name setter"""
        pass

    @property
    @abstractmethod
    def surname(self):
        """surname property"""
        pass

    @surname.setter
    @abstractmethod
    def surname(self, value):
        """surname setter"""
        pass

    @abstractmethod
    def insert_into_db(self):
        """Inserts instance into database"""
        pass

    @classmethod
    @abstractmethod
    def get_by_id(cls, id):
        """Class method that creates instance using database fields by id"""
        pass

    @abstractmethod
    def del_from_db(self):
        """Deletes instance from database"""
        pass

    @abstractmethod
    def get_courses(self):
        """Finds all courses of current teacher from database"""
        pass
