from abc import ABC, abstractmethod


class ICourse(ABC):
    """ Interface to represent Course """
    @property
    @abstractmethod
    def course_name(self):
        """course_name property"""
        pass

    @course_name.setter
    @abstractmethod
    def course_name(self, value):
        """course_name setter"""
        pass

    @property
    @abstractmethod
    def teacher(self):
        """teacher property"""
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value):
        """teacher setter"""
        pass

    @property
    @abstractmethod
    def course_program(self):
        """course_program property"""
        pass

    @course_program.setter
    @abstractmethod
    def course_program(self, value):
        """course_program setter"""
        pass

    @property
    @abstractmethod
    def type(self):
        """type property"""
        pass

    @type.setter
    @abstractmethod
    def type(self, value):
        """type setter"""
        pass

    @abstractmethod
    def insert_into_db(self):
        """ Inserts instance into database"""
        pass

    @abstractmethod
    def del_from_db(self):
        """ Deletes instance from database"""
        pass
