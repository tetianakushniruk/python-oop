import json


class Pizza:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string')
        self.__name = value

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

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value):
        if not isinstance(value, (tuple, list)) or not all(isinstance(x, str) for x in value):
            raise TypeError('Ingredients must be a tuple or list of strings!')
        self.__ingredients = list(x.lower() for x in value)

    def add_ingredient(self, new_ingredient):
        if not isinstance(new_ingredient, str):
            raise TypeError('Ingredient must a string!')
        if new_ingredient.lower() in self.ingredients:
            raise ValueError(f"Ingredient '{new_ingredient}' is already in pizza!")
        self.ingredients.append(new_ingredient)

    def del_ingredient(self, ingredient_to_del):
        if not isinstance(ingredient_to_del, str):
            raise TypeError('Ingredient must a string!')
        if ingredient_to_del.lower() not in self.ingredients:
            raise ValueError('There is no such ingredient in pizza!')
        self.__ingredients.remove(ingredient_to_del)

    def add_to_json(self):
        with open('pizza.json', 'r') as file:
            json_dict = json.load(file)
        json_dict['Custom'] = {'name': self.name, 'price': self.price,
                               'ingredients': self.ingredients}
        with open('pizza.json', 'w') as file:
            json.dump(json_dict, file, indent=4)

    def __str__(self):
        return f"Pizza\n" \
               f"   Name: {self.name}\n" \
               f"   Price: {self.price}\n" \
               f"   Ingredients: {self.ingredients}\n"


class MondayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return "Monday " + super().__str__()


class TuesdayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return "Tuesday " + super().__str__()


class WednesdayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return "Wednesday " + super().__str__()


class ThursdayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return "Thursday " + super().__str__()


class FridayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return "Friday " + super().__str__()


class SaturdayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return "Saturday " + super().__str__()


class SundayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return "Sunday " + super().__str__()
