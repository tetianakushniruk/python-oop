class Student:
    """
    Class used to represent information about a Student

    Attributes
    ----------
    name: str
        name of student
    surname: str
        surname of student
    record_book_num: int
        unique ID of student
    grades: list
        grades of student

    Methods
    -------
    average_score()
        counts average score of student
    """
    def __init__(self, name, surname, record_book_num, grades):
        """
        Parameters
        ----------
        name: str
            name of student
        surname: str
            surname of student
        record_book_num: int
            unique ID of student
        grades: list
            grades of student
        """
        self.name = name
        self.surname = surname
        self.record_book_num = record_book_num
        self.grades = grades

    @property
    def name(self):
        """Get name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Set name"""
        if not isinstance(value, str) or not value.strip():
            raise TypeError('Name must be a string!')
        self.__name = value

    @property
    def surname(self):
        """Get surname"""
        return self.__surname

    @surname.setter
    def surname(self, value):
        """Set surname"""
        if not isinstance(value, str) or not value.strip():
            raise TypeError('Surname must be a string!')
        self.__surname = value

    @property
    def record_book_num(self):
        """Get record_book_num"""
        return self.__record_book_num

    @record_book_num.setter
    def record_book_num(self, value):
        """Set record_book_num"""
        if not isinstance(value, int):
            raise TypeError('Number of record book must be an integer!')
        if value <= 0:
            raise ValueError('Number of record book must be more than zero!')
        self.__record_book_num = value

    @property
    def grades(self):
        """Get grades"""
        return self.__grades

    @grades.setter
    def grades(self, value):
        """Set grades"""
        if not isinstance(value, list):
            raise TypeError('Please enter grades of students as a list!')
        if not all(isinstance(x, int) for x in value):
            raise TypeError('Grades must be Integer type!')
        if not all(x > 0 for x in value):
            raise ValueError('Grades must be more than zero!')
        self.__grades = value

    def average_score(self):
        """Counts and returns average score of student"""
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        """Represents the class objects as a string"""
        return f'{self.name} {self.surname} {self.record_book_num} {self.grades}'

