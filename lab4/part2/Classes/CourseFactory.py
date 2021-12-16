from lab4.part2.Interfaces.ICourseFactory import ICourseFactory
from lab4.part2.Classes.LocalCourse import LocalCourse
from lab4.part2.Classes.OffsiteCourse import OffsiteCourse
from lab4.part2.Classes.Teacher import Teacher


class CourseFactory(ICourseFactory):
    @staticmethod
    def create_course(course_name, teacher_name, teacher_surname, course_program, type, additional_info):
        teacher = Teacher(teacher_name, teacher_surname)
        teacher.insert_into_db()
        courses = {
            'local': LocalCourse,
            'offsite': OffsiteCourse
        }
        course = courses[type](course_name, teacher, course_program, additional_info)
        course.insert_into_db()
        return course
