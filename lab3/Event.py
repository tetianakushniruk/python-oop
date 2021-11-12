from datetime import datetime


class Event:
    __all_ids = []

    def __init__(self, id, name, date, number_of_tickets, price):
        self.id = id
        self.name = name
        self.date = date
        self.number_of_tickets = number_of_tickets
        self.price = price

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError('ID must be an integer!')
        if value in self.__all_ids:
            raise ValueError('ID must be unique!')
        self.__all_ids.append(value)
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name of event must be a string!')
        self.__name = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError('Name of event must be a string!')
        try:
            datetime.strptime(value, '%d.%m.%Y')
        except:
            raise
        self.__date = value

    @property
    def number_of_tickets(self):
        return self.__number_of_tickets

    @number_of_tickets.setter
    def number_of_tickets(self, value):
        if not isinstance(value, int):
            raise TypeError('Quantity must be an integer!')
        if value <= 0:
            raise ValueError('Quantity must be more than 0!')
        self.__number_of_tickets = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Price must be a number!')
        if value <= 0:
            raise ValueError('Price must be more than 0!')
        self.__price = value

    def get_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'number_of_tickets': self.number_of_tickets,
            'price': self.price
        }

    def __str__(self):
        return f'   ID: {self.id}\n' \
               f'   Name: {self.name}\n' \
               f'   Date: {self.date}\n' \
               f'   Number of tickets: {self.number_of_tickets}\n' \
               f'   Regular price: {self.price}'
