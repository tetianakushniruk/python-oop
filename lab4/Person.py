import re


class Person:
    def __init__(self, name, surname, phone, birthday):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.birthday = birthday

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string')
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError('Surname must be a string')
        self.__surname = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if not isinstance(value, str):
            raise TypeError('Phone must be a string')
        phone_regex = re.compile('\\+[0-9]{12}')
        if not phone_regex.match(value):
            raise ValueError('Phone number pattern: +xxxxxxxxxxxx')
        self.__phone = value

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        if not isinstance(value, str):
            raise TypeError('Birthday must be a string')
        date_regex = re.compile('((0[1-9]|[12]\\d|3[01]).(0[1-9]|1[0-2]).[12]\\d{3})')
        if not date_regex.match(value):
            raise ValueError('Date pattern: dd.mm.yyyy')
        self.__birthday = value

    def __str__(self):
        return f'Name: {self.name}\n   Surname: {self.surname}\n' \
               f'   Phone number {self.phone}\n   Birthday: {self.birthday}'

