import re


class Customer:
    """
    Class used to represent information about a Customer

    Attributes
    ----------
    surname: str
        surname of customer
    name: str
        name of customer
    patronymic: str
        patronymic of customer
    phone: str
        mobile phone of customer. must match the pattern
    """
    def __init__(self, surname, name, patronymic, phone):
        """
        Parameters
        ----------
        surname: str
            surname of customer
        name: str
            name of customer
        patronymic: str
            patronymic of customer
        phone: str
            mobile phone of customer. must match the pattern
        """
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    @property
    def surname(self):
        """Get surname"""
        return self.__surname

    @property
    def name(self):
        """Get name"""
        return self.__name

    @property
    def patronymic(self):
        """Get patronymic"""
        return self.__patronymic

    @property
    def phone(self):
        """Get phone"""
        return self.__phone

    @surname.setter
    def surname(self, value):
        """Set surname"""
        if not isinstance(value, str) or not value.strip():
            raise TypeError('Surname must be a string!')
        else:
            self.__surname = value

    @name.setter
    def name(self, value):
        """Set name"""
        if not isinstance(value, str) or not value.strip():
            raise TypeError('Name must be a string!')
        else:
            self.__name = value

    @patronymic.setter
    def patronymic(self, value):
        """Set patronymic"""
        if not isinstance(value, str) or not value.strip():
            raise TypeError('Patronymic must be a string!')
        else:
            self.__patronymic = value

    @phone.setter
    def phone(self, value):
        """Set phone"""
        phone_regex = re.compile('^\\+[0-9]{3}\\((\\d{2})\\)-\\d{3}-\\d{2}-\\d{2}')
        if not phone_regex.match(value):
            raise TypeError('Phone number pattern: +380(96)-xx-xxx-xx-xx')
        else:
            self.__phone = value

    def __str__(self):
        """Represents the class objects as a string"""
        return f'{self.surname} {self.name} {self.patronymic}, {self.phone}'
