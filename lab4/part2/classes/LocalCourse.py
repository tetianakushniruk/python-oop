from lab4.part2.interfaces.ILocalCourse import ILocalCourse
from lab4.part2.classes.Course import Course
from lab4.part2.db.models import *


class LocalCourse(Course, ILocalCourse):
    """ Class to represent LocalCourse

    Inherits class Course, extends Course attributes with its own attribute lab_number

    Attributes
    ----------
    lab_number: int
        laboratory number

    Methods
    -------
    insert_into_db():
        inserts instance into database
    """
    def __init__(self, course_name, teacher, course_program, lab_number):
        """
        Parameters
        ----------
        course_name: str
            name of the course
        teacher: Teacher
            teacher of the course
        course_program: list
            list of topics
        lab_number: int
            laboratory number
        """
        super().__init__(course_name, teacher, course_program, 'local')
        self.lab_number = lab_number

    @property
    def lab_number(self):
        """Lab_number property"""
        return self.__lab_number

    @lab_number.setter
    def lab_number(self, value):
        """Lab_number setter"""
        if not isinstance(value, int):
            raise TypeError
        if value <= 0:
            raise ValueError
        self.__lab_number = value

    def insert_into_db(self):
        """Inserts instance into database

        Calls method insert_into_db() of super class, then adds lab_number to the database.
        """
        super().insert_into_db()
        session = sessionmaker(bind=engine)
        s = session()
        s.query(CourseTable).filter(CourseTable.course_name == self.course_name)\
            .update({CourseTable.lab_number: self.lab_number})
        s.commit()

    def __str__(self):
        """Represents attributes as a string"""
        return super().__str__() + f'Number of laboratory: {self.lab_number}'
