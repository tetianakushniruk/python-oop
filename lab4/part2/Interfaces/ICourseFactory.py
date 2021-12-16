from abc import ABC, abstractmethod


class ICourseFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_course(course_name, teacher_name, teacher_surname, course_program, type, additional_info):
        pass
