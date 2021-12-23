from sqlalchemy import and_
from lab4.part2.interfaces.ITeacher import ITeacher
from lab4.part2.db.models import *


class Teacher(ITeacher):
    """ Class to represent Teacher

    Attributes
    ----------
    name: str
        name of teacher
    surname: str
        surname of teacher

    Methods
    -------
    insert_into_db():
        inserts instance into database
    get_by_id(id):
        class method that creates instance using database fields by id
    del_from_db():
        deletes instance from database
    get_courses():
        finds all courses of current teacher from database
    """
    def __init__(self, name, surname):
        """

        Parameters
        ----------
        name: str
            name of teacher
        surname: str
            surname of teacher
        """
        self.name = name
        self.surname = surname

    @property
    def name(self):
        """name property"""
        return self.__name

    @name.setter
    def name(self, value):
        """name setter"""
        if not isinstance(value, str):
            raise TypeError
        self.__name = value

    @property
    def surname(self):
        """surname property"""
        return self.__surname

    @surname.setter
    def surname(self, value):
        """surname setter"""
        if not isinstance(value, str):
            raise TypeError
        self.__surname = value

    def insert_into_db(self):
        """Inserts instance into database

        Checks if such a teacher already exists in the database.
        If not, instantiates TeacherTable from self attributes and adds it to the database.
        """
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
        """Class method that creates instance using database fields by id

        Gets a TeacherTable object from the database by id.
        Then creates an instance of the Teacher class and returns it.

        Parameters
        ----------
        id: int
            id of teacher to get from database

        Returns
        -------
        Teacher object created using fields of database by particular id.
        """
        session = sessionmaker(bind=engine)
        s = session()
        teacher = s.query(TeacherTable).get(id)
        return cls(teacher.name, teacher.surname)

    def del_from_db(self):
        """Deletes instance from database

        Searches the database for a teacher by name and surname and then deletes the teacher.
        """
        session = sessionmaker(bind=engine)
        s = session()
        s.query(TeacherTable).filter(and_(TeacherTable.name == self.name,
                                          TeacherTable.surname == self.surname)).delete()
        s.commit()

    def get_courses(self):
        """Finds all courses of current teacher from database

        Returns
        -------
        List of course ids taught by the teacher.
        """
        session = sessionmaker(bind=engine)
        s = session()
        find_courses = s.query(teacher_course).join(TeacherTable).filter(and_(TeacherTable.name == self.name,
                                                                  TeacherTable.surname == self.surname))
        return [y for (x, y) in find_courses]

    def __str__(self):
        """Represents attributes as a string"""
        return f'Name: {self.name}. Surname: {self.surname}'
