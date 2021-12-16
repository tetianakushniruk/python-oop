from models import *

session = sessionmaker(bind=engine)
s = session()

teachers = [TeacherTable('Madelyn', 'Ramirez'), TeacherTable('Connie', 'Smith'), TeacherTable('Victoria', 'Mcintyre'),
            TeacherTable('Adam', 'Morrow'), TeacherTable('Ashley', 'Crawford'), TeacherTable('Amanda', 'Mcmahon'),
            TeacherTable('Richard', 'Lang'), TeacherTable('Corey', 'Perez'), TeacherTable('Angela', 'Eaton'),
            TeacherTable('David', 'Jackson'), TeacherTable('Trevor', 'Lucas'), TeacherTable('Teresa', 'Mcgee'),
            TeacherTable('Brittany', 'Ramos'), TeacherTable('Valerie', 'Schneider'), TeacherTable('Edward', 'Williams'),
            TeacherTable('Brian', 'Miller'), TeacherTable('Todd', 'Molina'), TeacherTable('Stephen', 'Harris'),
            TeacherTable('Alison', 'Jones'), TeacherTable('Allison', 'Solomon')]

courses = [CourseTable('AI on Microsoft Azure', 5, 'Python, ASR systems, NLP, computer vision ',
                       'local', 15, None),
           CourseTable('Cyber Security Training', 3, 'password security, network security, OWASP',
                       'offsite', None, 'London'),
           CourseTable('Data Analytics Using Python', 10, 'data analysis,  Python, data wrangling',
                       'local', 15, None),
           CourseTable('AI Design and Engineering', 5, 'cloud computing, AI programming, math',
                       'local', 2, None),
           CourseTable('Software Development Fundamentals', 16, 'project management, programming',
                       'offsite', None, 'Edinburgh')]

s.add_all(teachers)
s.add_all(courses)

# relations
for teacher_id in range(len(teachers)):
    teacher = teachers[teacher_id]
    for course in courses:
        if teacher_id + 1 == course.teacher_id:
            teacher.courses.append(course)

s.commit()
