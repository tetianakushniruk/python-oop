import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///D:\\kpi\\2\\oop\\labs\\lab4\\part2\\db\\db.db', echo=True)
connection = engine.connect()

Base = declarative_base(bind=engine)

teacher_course = Table(
    "teacher_course",
    Base.metadata,
    Column("teacher_id", Integer, ForeignKey("teacher.teacher_id")),
    Column("course_id", Integer, ForeignKey("course.course_id")),
)


class TeacherTable(Base):
    """Class to represent table Teacher

    Attributes
    ----------
    name: str
        name of teacher
    surname: str
        surname of teacher
    """
    __tablename__ = "teacher"
    teacher_id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    courses = relationship("CourseTable", secondary=teacher_course, back_populates="teacher")

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class CourseTable(Base):
    """Class to represent table Teacher

    Attributes
    ----------
    course_name: str
        name of the course
    teacher_id: int
        teacher of the course
    course_program: string
        course topics separated by commas
    type: str
        type of the course
    lab_number: int
        laboratory number
    place: str
        place where the course is held
    """
    __tablename__ = "course"
    course_id = Column(Integer, primary_key=True)
    course_name = Column(String)
    teacher_id = Column(Integer, ForeignKey("teacher.teacher_id"))
    course_program = Column(String)
    type = Column(String)
    lab_number = Column(Integer)
    place = Column(String)
    teacher = relationship("TeacherTable", secondary=teacher_course, back_populates="courses")

    def __init__(self, course_name, teacher_id, course_program, type, lab_number=None, place=None):
        self.course_name = course_name
        self.teacher_id = teacher_id
        self.course_program = course_program
        self.type = type
        self.lab_number = lab_number
        self.place = place


Base.metadata.create_all()
