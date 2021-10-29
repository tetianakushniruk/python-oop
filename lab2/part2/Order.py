from Product import Product
from collections import Counter


class Order:
    """
    Class used to represent information about an Order

    Attributes
    ----------
    dict_of_products: dict
        dictionary where keys are elements of Product type and values are number of this products in order
    customer_info: Customer
        information about customer

    Methods
    -------
    total_order_value()
        returns total cost of the order
    add_product(new_product, quantity)
        adds new product to order
    change_quantity(product_code, quantity=0)
        changes quantity of certain product in order or deletes it
    """
    def __init__(self, dict_of_products, customer_info):
        """
        Parameters
        ----------
        dict_of_products: dict
            dictionary where keys are elements of Product type and values are number of this products in order
        customer_info: Customer
            information about customer
        """
        self.dict_of_products = dict_of_products
        self.customer_info = customer_info

    @property
    def dict_of_products(self):
        """Get dict_of_products"""
        return self.dict_of_products

    @dict_of_products.setter
    def dict_of_products(self, value):
        """Set dict_of_products"""
        self.__check_for_duplicates(value)
        self.__dict_of_products = value

    @staticmethod
    def __check_for_duplicates(dict_of_products):
        """Checks for duplicates of products codes in dict_of_products

        Builds list of all codes and counts the number of occurrences of each code

        Parameters
        ----------
        dict_of_products: dict
            dictionary where keys are elements of Product type and values are number of this products in order

        Raises
        ------
        ValueError
            if any of the codes occurs more than once
        """
        list_of_codes = [i.product_code for i in dict_of_products.keys()]
        for count in Counter(list_of_codes).values():
            if count != 1:
                raise ValueError('Product codes must be unique!')

    def total_order_value(self):
        """Returns total cost of the order"""
        total_order_value = 0
        for key in self.__dict_of_products:
            total_order_value += key.price * self.__dict_of_products[key]
        return total_order_value

    def add_product(self, new_product, quantity):
        """Adds new product to order

        Parameters
        ----------
        new_product: Product
            product that should be added to order
        quantity: int
            quantity of certain product in order

        Raises
        ------
        TypeError
            if quantity is not int or new_product is not Product type
        ValueError
            if quantity is less or equal to zero
        """
        if not isinstance(new_product, Product):
            raise TypeError('Object must be Product type')
        if not isinstance(quantity, int):
            raise TypeError('Quantity must be integer')
        if quantity <= 0:
            raise ValueError('Quantity must be more than 0')
        self.__dict_of_products[new_product] = quantity

    def change_quantity(self, product_code, quantity=0):
        """Changes quantity of certain product in order or deletes it

        Parameters
        ----------
        product_code: int
            product that should be deleted or quantity of which should be changed
        quantity: int, optional
            new quantity(default is 0)

        Raises
        ------
        TypeError
            if product_code or quantity is not int
        ValueError
            if quantity is less than 0
        KeyError
            if there is no product with such code in order
        """
        if not isinstance(product_code, int):
            raise TypeError('Product code must be Integer type')
        if not isinstance(quantity, int):
            raise TypeError('Quantity must be integer')
        if quantity < 0:
            raise ValueError('Quantity must not be less than 0')
        key = None
        for i in self.__dict_of_products.keys():
            if i.product_code == product_code:
                key = i
        try:
            if not quantity:
                del self.__dict_of_products[key]
            else:
                self.__dict_of_products[key] = quantity
        except KeyError:
            print('There is no such product in the order')

    def __str__(self):
        """Represents the class objects as a string"""
        dict_str = '\n'.join([f'  Product info:\n     {key}\n     Quantity: {value}'
                              for (key, value) in self.__dict_of_products.items()])
        return f'~~~~~~~Order info~~~~~~~\n  Customer info:\n     {self.customer_info}\n{dict_str}\n' \
               f'Total order value: {self.total_order_value()}'
