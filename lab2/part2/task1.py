class Product:
    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions

    @property
    def price(self):
        return self.__price

    @property
    def description(self):
        return self.__description

    @property
    def dimensions(self):
        return self.__dimensions

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Price must be a number!')
        elif value <= 0.:
            raise ValueError('Price cannot be less than or equal to 0')
        else:
            self.__price = value

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError('Description must be a string!')
        else:
            self.__description = value

    @dimensions.setter
    def dimensions(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Dimensions must be a number!')
        elif value <= 0.:
            raise ValueError('Dimensions cannot be less than or equal to 0')
        else:
            self.__dimensions = value

    def __str__(self):
        return f'Price: {self.price}. Description: {self.description}. Dimensions: {self.dimensions}'


class Customer:
    def __init__(self, surname, name, patronymic, phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def phone(self):
        return self.__phone

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError('Surname must be a string!')
        else:
            self.__surname = value

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string!')
        else:
            self.__name = value

    @patronymic.setter
    def patronymic(self, value):
        if not isinstance(value, str):
            raise TypeError('Patronymic must be a string!')
        else:
            self.__patronymic = value

    @phone.setter
    def phone(self, value):
        if not isinstance(value, str) or value[0] != '+':
            raise TypeError('Phone number must be a string that starts with + and country code. Example: +380......')
        else:
            self.__phone = value

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}, {self.phone}'


class Order:
    # dict_of_products - dictionary where keys are elements of Product type
    # and values are number of this products in order
    def __init__(self, dict_of_products, customer_info):
        self.__dict_of_products = dict_of_products
        self.__customer_info = customer_info
        self.__total_order_value = 0

    @property
    def total_order_value(self):
        for key in self.__dict_of_products:
            self.__total_order_value += key.price * self.__dict_of_products[key]
        return self.__total_order_value

    def __str__(self):
        dict_str = '\n'.join([f'  Product info:\n     {key}\n     Quantity: {value}'
                              for (key, value) in self.__dict_of_products.items()])
        return f'~~~~~~~Order info~~~~~~~\n  Customer info:\n     {self.__customer_info}\n{dict_str}\n' \
               f'Total order value: {self.total_order_value}'


if __name__ == '__main__':
    product1 = Product(250, 'Phone', 350)
    product2 = Product(524, 'Laptop', 1596)
    customer1 = Customer('Kushniruk', 'Tatiana', 'Alexandrovna', '+380969874634')
    order1 = Order({product1: 2, product2: 5}, customer1)
    print(order1)
