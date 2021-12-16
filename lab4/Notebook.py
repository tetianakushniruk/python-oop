from Person import Person


class Notebook:
    def __init__(self, list_of_people=None):
        if list_of_people is None:
            list_of_people = []
        self.list_of_people = list_of_people

    @property
    def list_of_people(self):
        return self.__list_of_people

    @list_of_people.setter
    def list_of_people(self, value):
        if not isinstance(value, list):
            raise TypeError('Value must be a list')
        if value and not all(isinstance(x, Person) for x in value):
            raise TypeError('Elements of list must be Person type')
        self.__list_of_people = value

    def __add__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        new_list = self.list_of_people.copy()
        new_list.append(other)
        return Notebook(new_list)

    def __iadd__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        self.list_of_people.append(other)
        return self

    def __sub__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        new_list = self.list_of_people.copy()
        new_list.remove(other)
        return Notebook(new_list)

    def __isub__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        self.list_of_people.remove(other)
        return self

    def __mul__(self, other):
        if isinstance(other, Person) and other in self.list_of_people:
            return other
        for x in self.list_of_people:
            if other in x.__dict__.values():
                return x
        return NotImplemented

    def __str__(self):
        if not self.list_of_people:
            return 'List is empty'
        list_str = '\n'.join(f'{i}. {x}' for (i, x) in enumerate(self.list_of_people, start=1))
        return list_str
