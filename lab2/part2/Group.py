from Student import Student
from collections import Counter


class Group:
    """
    Class used to represent information about an Order

    Attributes
    ----------
    list_of_students: list
        contains list of all students in the group

    Methods
    -------
    add_student(student)
        adds new student to the list
    del_student(student):
        deletes certain student from list
    list_of_top_students()
        makes list of students sorted by average score
    top_of_students(quantity)
        returns list of certain number of top students as a string
    """
    def __init__(self, list_of_students):
        """
        Parameters
        ----------
        list_of_students: list
            contains list of all students in the group
        """
        self.list_of_students = list_of_students

    @property
    def list_of_students(self):
        return self.__list_of_students

    @list_of_students.setter
    def list_of_students(self, value):
        if not isinstance(value, list):
            raise TypeError('Enter students as a list')
        if len(value) > 20:
            raise ValueError('The number of students in group must not be more than 20!')
        if not all(isinstance(x, Student) for x in value):
            raise TypeError('Entered arguments must be Student type!')
        Group.__check_for_duplicates(value)
        self.__list_of_students = value

    @staticmethod
    def __check_for_duplicates(list_of_students):
        """Checks for duplicates in list of students

        Builds lists of all student names and IDs and counts the number of their occurrences

        Parameters
        ----------
        list_of_students: list
            contains list of all students in the group

        Raises
        ------
        ValueError
            if there are students with same names of IDs in list
        """
        list_of_names = [i.name + ' ' + i.surname for i in list_of_students]
        for count in Counter(list_of_names).values():
            if count != 1:
                raise ValueError('There cannot be students with the same name and surname in a group!')
        list_of_record_book_nums = [i.record_book_num for i in list_of_students]
        for count in Counter(list_of_record_book_nums).values():
            if count != 1:
                raise ValueError('There cannot be students with the same record book number in a group!')

    def add_student(self, student):
        """Adds new student to the list

        Parameters
        ----------
        student: Student
            contains info about new student

        Raises
        ------
        TypeError
            if parameter is not Student type
        ValueError
            if there is already student with the same name or ID in list
            or if the maximum number of students in group has been reached
        """
        if not isinstance(student, Student):
            raise TypeError('Parameter must be Student type!')
        for i in self.list_of_students:
            if student.name == i.name and student.surname == i.surname:
                raise ValueError('There is already student with the same name in group!')
            if student.record_book_num == i.record_book_num:
                raise ValueError('Number of record book must be unique!')
        if len(self.list_of_students) == 20:
            raise ValueError('The maximum number of students in group has been reached!')
        self.list_of_students.append(student)

    def del_student(self, student):
        """Deletes certain student from list

        Parameters
        ----------
        student: Student
            student that should be deleted

        Raises
        ------
        TypeError
            if parameter is not Student type
        ValueError
            if there is no such student in group
        """
        if not isinstance(student, Student):
            raise TypeError('Parameter must be Student type')
        try:
            self.list_of_students.remove(student)
        except ValueError:
            print('There is no such student in group')

    def list_of_top_students(self):
        """Makes and returns list of students sorted by average score"""
        top = [[str(i), i.average_score()] for i in self.list_of_students]
        top.sort(key=lambda x: x[1], reverse=True)
        return top

    def top_of_students(self, quantity):
        """Returns list of certain number of top students as a string"""
        if quantity > 20:
            raise ValueError("The maximum number of students in group is 20!")
        top = self.list_of_top_students()
        top_str = '\n'.join(f"{i+1}) {x:<40}" + f"{'Score: ': >5}" + f"{y:.1f}"
                            for i, (x, y) in enumerate(top[:quantity]))
        return f'~~Top {quantity}~~\n{top_str}'
