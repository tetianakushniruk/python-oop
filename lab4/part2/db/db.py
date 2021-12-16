import sqlite3

connect = sqlite3.connect('db.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS course
                (course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT NOT NULL,
                teacher_id INTEGER,
                course_program TEXT NOT NULL,
                type TEXT NOT NULL,
                lab_number INTEGER,
                place TEXT)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS teacher
                (teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL)
""")

teachers = [('Madelyn', 'Ramirez'), ('Connie', 'Smith'), ('Victoria', 'Mcintyre'), ('Adam', 'Morrow'),
            ('Ashley', 'Crawford'), ('Amanda', 'Mcmahon'), ('Richard', 'Lang'), ('Corey', 'Perez'),
            ('Angela', 'Eaton'), ('David', 'Jackson'), ('Trevor', 'Lucas'), ('Teresa', 'Mcgee'),
            ('Brittany', 'Ramos'), ('Valerie', 'Schneider'), ('Edward', 'Williams'), ('Brian', 'Miller'),
            ('Todd', 'Molina'), ('Stephen', 'Harris'), ('Alison', 'Jones'), ('Allison', 'Solomon')]

cursor.executemany("INSERT INTO teacher(name, surname) VALUES(?, ?);", teachers)

courses = [('AI on Microsoft Azure', 5, 'Python, ASR systems, NLP, computer vision ', 'local', 15, None),
           ('Cyber Security Training', 3, 'password security, network security, OWASP', 'offsite', None, 'London'),
           ('Data Analytics Using Python', 10, 'data analysis,  Python, data wrangling', 'local', 15, None),
           ('AI Design and Engineering', 5, 'cloud computing, AI programming, math', 'local', 2, None),
           ('Software Development Fundamentals', 16, 'project management, programming', 'offsite', None, 'Edinburgh')]

cursor.executemany("INSERT INTO course(course_name, teacher_id, course_program, type, lab_number, place)"
                   " VALUES(?, ?, ?, ?, ?, ?);", courses)

connect.commit()
