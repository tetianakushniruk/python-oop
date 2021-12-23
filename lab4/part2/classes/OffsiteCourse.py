from sqlalchemy import and_

from lab4.part2.interfaces.IOffsiteCourse import IOffsiteCourse
from lab4.part2.classes.Course import Course
from lab4.part2.db.models import *


class OffsiteCourse(Course, IOffsiteCourse):
    """Class to represent OffsiteCourse

    Inherits class Course, extends Course attributes with its own attribute place

    Attributes
    ----------
    place: str
        place where the course is held

    Methods
    -------
    insert_into_db():
        inserts instance into database
    """
    def __init__(self, course_name, teacher, course_program, place):
        """
        Parameters
        ----------
        course_name: str
            name of the course
        teacher: Teacher
            teacher of the course
        course_program: list
            list of topics
        place: str
            place where the course is held
        """
        super().__init__(course_name, teacher, course_program, 'offsite')
        self.place = place

    @property
    def place(self):
        """place property"""
        return self.__place

    @place.setter
    def place(self, value):
        """place setter"""
        if not isinstance(value, str):
            raise TypeError
        self.__place = value

    def insert_into_db(self):
        """Inserts instance into database

        Calls method insert_into_db() of super class, then adds place to the database.
        """
        super().insert_into_db()
        session = sessionmaker(bind=engine)
        s = session()
        s.query(CourseTable).filter(CourseTable.course_name == self.course_name) \
            .update({CourseTable.place: self.place})
        s.commit()

    def __str__(self):
        """Represents attributes as a string"""
        return super().__str__() + f'Place: {self.place}'
