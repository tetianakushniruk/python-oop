from sqlalchemy import and_
from lab4.part2.Interfaces.ITeacher import ITeacher
from lab4.part2.db.models import *


class Teacher(ITeacher):

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__surname = value

    def insert_into_db(self):
        session = sessionmaker(bind=engine)
        s = session()
        teacher = (s.query(TeacherTable)
                   .filter(and_(TeacherTable.name == self.name,
                                TeacherTable.surname == self.surname))
                   .one_or_none())
        if teacher is None:
            s.add(TeacherTable(self.name, self.surname))
            s.commit()

    @classmethod
    def get_by_id(cls, id):
        session = sessionmaker(bind=engine)
        s = session()
        teacher = s.query(TeacherTable).get(id)
        return cls(teacher.name, teacher.surname)

    def del_from_db(self):
        session = sessionmaker(bind=engine)
        s = session()
        s.query(TeacherTable).filter(and_(TeacherTable.name == self.name,
                                          TeacherTable.surname == self.surname)).delete()
        s.commit()

    def get_courses(self):
        session = sessionmaker(bind=engine)
        s = session()
        find_courses = s.query(teacher_course).join(TeacherTable).filter(and_(TeacherTable.name == self.name,
                                                                  TeacherTable.surname == self.surname))
        return [y for (x, y) in find_courses]

    def __str__(self):
        return f'Name: {self.name}. Surname: {self.surname}'
