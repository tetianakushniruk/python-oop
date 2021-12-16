from abc import ABC, abstractmethod


class ICourse(ABC):
    @property
    @abstractmethod
    def course_name(self):
        pass

    @course_name.setter
    @abstractmethod
    def course_name(self, value):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value):
        pass

    @property
    @abstractmethod
    def course_program(self):
        pass

    @course_program.setter
    @abstractmethod
    def course_program(self, value):
        pass

    @property
    @abstractmethod
    def type(self):
        pass

    @type.setter
    @abstractmethod
    def type(self, value):
        pass

    @abstractmethod
    def insert_into_db(self):
        pass

    @abstractmethod
    def del_from_db(self):
        pass
