from sqlalchemy import and_

from lab4.part2.Interfaces.ILocalCourse import ILocalCourse
from lab4.part2.Classes.Course import Course
from lab4.part2.db.models import *


class LocalCourse(Course, ILocalCourse):
    def __init__(self, course_name, teacher, course_program, lab_number):
        super().__init__(course_name, teacher, course_program, 'local')
        self.lab_number = lab_number

    @property
    def lab_number(self):
        return self.__lab_number

    @lab_number.setter
    def lab_number(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value <= 0:
            raise ValueError
        self.__lab_number = value

    def insert_into_db(self):
        super().insert_into_db()
        session = sessionmaker(bind=engine)
        s = session()
        s.query(CourseTable).filter(CourseTable.course_name == self.course_name)\
            .update({CourseTable.lab_number: self.lab_number})
        s.commit()

    def __str__(self):
        return super().__str__() + f'Number of laboratory: {self.lab_number}'
