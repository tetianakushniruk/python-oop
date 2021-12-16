from sqlalchemy import and_

from lab4.part2.Interfaces.IOffsiteCourse import IOffsiteCourse
from lab4.part2.Classes.Course import Course
from lab4.part2.db.models import *


class OffsiteCourse(Course, IOffsiteCourse):
    def __init__(self, course_name, teacher_id, course_program, place):
        super().__init__(course_name, teacher_id, course_program, 'offsite')
        self.place = place

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__place = value

    def insert_into_db(self):
        super().insert_into_db()
        session = sessionmaker(bind=engine)
        s = session()
        s.query(CourseTable).filter(CourseTable.course_name == self.course_name) \
            .update({CourseTable.place: self.place})
        s.commit()

    def __str__(self):
        return super().__str__() + f'Place: {self.place}'
