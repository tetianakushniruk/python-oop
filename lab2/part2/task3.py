from Student import Student
from Group import Group

if __name__ == '__main__':
    student1 = Student('tania', 'kushniruk', 486, [5, 5])
    student2 = Student('vasya', 'pupkin', 652, [5, 1, 3])
    student3 = Student('tania', 'kushnir', 481, [1, 3, 1])
    student4 = Student('federico', 'fellini', 236, [5, 5, 5])
    student5 = Student('python', 'pythonov', 621, [1])
    group1 = Group([student1, student2, student3])
    group1.add_student(student4)
    group1.add_student(student5)
    print(group1.top_of_students(5))

