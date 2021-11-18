import json
from datetime import datetime


class Ticket:
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
        if value < 0:
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

    def return_ticket(self):
        with open('events.json', 'r') as file:
            json_dict = json.load(file)
        dict_of_attributes = json_dict[str(self.id)]
        dict_of_attributes['number_of_tickets'] += 1
        json_dict[str(self.id)] = dict_of_attributes
        with open('events.json', 'w') as file:
            json.dump(json_dict, file, indent=4)
        print('Ticket was returned!')
        self.number_of_tickets += 1

    @classmethod
    def construct_by_id(cls, id):
        with open('events.json', 'r') as file:
            json_dict = json.load(file)
            try:
                dict_of_attributes = json_dict[str(id)]
            except:
                raise
        if not dict_of_attributes['number_of_tickets']:
            raise ValueError('Tickets for this event have run out!')
        dict_of_attributes['number_of_tickets'] -= 1
        json_dict[str(id)] = dict_of_attributes
        with open('events.json', 'w') as file:
            json.dump(json_dict, file, indent=4)
        return cls(id, dict_of_attributes['name'], dict_of_attributes['date'],
                   dict_of_attributes['number_of_tickets'], dict_of_attributes['price'])

    def __str__(self):
        return f'{self.name}\n' \
                   f'   ID: {self.id}\n' \
                   f'   Date: {self.date}\n' \
                   f'   Remaining number of tickets: {self.number_of_tickets}\n' \
                   f'   Price: {self.price}'


class AdvanceTicket(Ticket):
    def __init__(self, id, name, date, number_of_tickets, price):
        super().__init__(id, name, date, number_of_tickets, price)
        self.price = self.price * 0.6


class StudentTicket(Ticket):
    def __init__(self, id, name, date, number_of_tickets, price):
        super().__init__(id, name, date, number_of_tickets, price)
        self.price = self.price * 0.5


class LateTicket(Ticket):
    def __init__(self, id, name, date, number_of_tickets, price):
        super().__init__(id, name, date, number_of_tickets, price)
        self.price = self.price * 1.1
