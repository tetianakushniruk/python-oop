class Student:
    def __init__(self, name, surname, **kwargs):
        self.name = name
        self.surname = surname
        self.__dict__.update(kwargs)

    def __str__(self):

        return ', '.join(tmp)


if __name__ == '__main__':
    stud = Student('Tom', 'FTGYUHI', age=15, weight=65)
    print(stud)