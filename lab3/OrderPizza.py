from datetime import datetime
import calendar
import json
from Pizza import *


class OrderPizza:
    def __init__(self, quantity, day, pizza=None):
        self.quantity = quantity
        if not day:
            day = list(calendar.day_name)[datetime.today().weekday()]
        elif pizza:
            raise ValueError('You cannot choose pizza of the day and create your own at the same time')
        self.day = day
        if not pizza:
            pizza = self.get_pizza()
        self.pizza = pizza

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise TypeError('Quantity must be an integer!')
        if value <= 0:
            raise ValueError('Quantity must be more than 0!')
        self.__quantity = value

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if not isinstance(value, str):
            raise TypeError('Weekday must be a string!')
        if value not in list(calendar.day_name):
            raise ValueError("It's not a weekday!")
        self.__day = value

    @property
    def pizza(self):
        return self.__pizza

    @pizza.setter
    def pizza(self, value):
        if not isinstance(value, Pizza):
            raise TypeError('Value must be Pizza type!')
        self.__pizza = value

    def get_pizza(self):
        classes_dict = {
            'Monday': MondayPizza,
            'Tuesday': TuesdayPizza,
            'Wednesday': WednesdayPizza,
            'Thursday': ThursdayPizza,
            'Friday': FridayPizza,
            'Saturday': SaturdayPizza,
            'Sunday': SundayPizza
        }
        with open('pizza.json', 'r') as file:
            json_dict = json.load(file)
            try:
                dict_of_pizza = json_dict[self.day]
            except:
                raise
        return classes_dict[self.day](dict_of_pizza['name'], dict_of_pizza['price'],
                                      dict_of_pizza['ingredients'])

    def __str__(self):
        return str(self.pizza) + f'Quantity: {self.quantity}'
