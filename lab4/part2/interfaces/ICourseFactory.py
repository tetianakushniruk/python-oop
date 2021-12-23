from abc import ABC, abstractmethod


class ICourseFactory(ABC):
    """ Interface to represent CourseFactory """
    @staticmethod
    @abstractmethod
    def create_course(course_name, teacher_name, teacher_surname, course_program, type, additional_info):
        """Static method that creates instance depending on type of the course"""
        pass
