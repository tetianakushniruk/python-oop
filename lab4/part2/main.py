from lab4.part2.classes.CourseFactory import CourseFactory

if __name__ == '__main__':
    course1 = CourseFactory.create_course('Database Design and Basic SQL in PostgreSQL', 'Blaine',
                                          'West', ['Introduction to SQL', 'One-to-Many Data Models',
                                                   'Many-To-Many Data Models'], 'local', 32)

