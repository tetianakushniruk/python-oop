from sqlalchemy import and_

from lab4.part2.Interfaces.ICourse import ICourse
from lab4.part2.Classes.Teacher import Teacher
from lab4.part2.db.models import *


class Course(ICourse):
    def __init__(self, course_name, teacher, course_program, type):
        self.course_name = course_name
        self.teacher = teacher
        self.course_program = course_program
        self.type = type

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__course_name = value

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError
        self.__teacher = value

    @property
    def course_program(self):
        return self.__course_program

    @course_program.setter
    def course_program(self, value):
        if not isinstance(value, list):
            raise TypeError
        if not all(isinstance(x, str) for x in value):
            raise TypeError
        self.__course_program = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if not isinstance(value, str):
            raise TypeError
        if value not in ('local', 'offsite'):
            raise ValueError
        self.__type = value

    def insert_into_db(self):
        session = sessionmaker(bind=engine)
        s = session()
        course = (s.query(CourseTable)
                  .filter(CourseTable.course_name == self.course_name).one_or_none())
        if course is None:
            teacher_id = s.query(TeacherTable.teacher_id)\
                .filter(and_(TeacherTable.name == self.teacher.name,
                             TeacherTable.surname == self.teacher.surname))
            course_program = ', '.join(x for x in self.course_program)
            s.add(CourseTable(self.course_name, teacher_id, course_program, self.type))
            s.commit()

    def del_from_db(self):
        session = sessionmaker(bind=engine)
        s = session()
        s.query(CourseTable).filter(CourseTable.course_name == self.course_name).delete()
        s.commit()

    def __str__(self):
        return f'Course name: {self.course_name}. Teacher: {self.teacher}. ' \
               f'Course program: {self.course_program}. Type: {self.type}. '
