from lab4.part2.interfaces.ICourseFactory import ICourseFactory
from lab4.part2.classes.LocalCourse import LocalCourse
from lab4.part2.classes.OffsiteCourse import OffsiteCourse
from lab4.part2.classes.Teacher import Teacher


class CourseFactory(ICourseFactory):
    """ Class to represent CourseFactory """
    @staticmethod
    def create_course(course_name, teacher_name, teacher_surname, course_program, type, additional_info):
        """Instantiates Course

        Instantiates Teacher and adds to the database if not already exists.
        Then creates Course depending on type (LocalCourse/OffsiteCourse) and
        adds it to the database if not already exists.

        Parameters
        ---------
        course_name: str
            name of the course
        teacher_name: str
            name of teacher
        teacher_surname: str
            surname of teacher
        course_program: list
            list of topics
        type: str
            type of the course
        additional_info:
            lab_number or place where the course is held

        Returns
        -------
        Course instance
        """
        teacher = Teacher(teacher_name, teacher_surname)
        teacher.insert_into_db()
        courses = {
            'local': LocalCourse,
            'offsite': OffsiteCourse
        }
        course = courses[type](course_name, teacher, course_program, additional_info)
        course.insert_into_db()
        return course
