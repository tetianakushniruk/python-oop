class Product:
    """
    Class used to represent information about a Product

    Attributes
    ----------
    product_code: int
        unique ID of product
    price: int, float
        price of one unit of product
    description: str
        short description of product(for example, name or model)
    dimensions: int, float
        dimensions of product(for example, size or weight)
    """
    def __init__(self, product_code, price, description, dimensions):
        """
        Parameters
        ----------
        product_code: int
            unique id of product
        price: int, float
            price of one unit of product
        description: str
            short description of product(for example, name or model)
        dimensions: int, float
            dimensions of product(for example, size or weight)
        """
        self.product_code = product_code
        self.price = price
        self.description = description
        self.dimensions = dimensions

    @property
    def product_code(self):
        """Get product_code"""
        return self.__product_code

    @property
    def price(self):
        """Get price"""
        return self.__price

    @property
    def description(self):
        """Get description"""
        return self.__description

    @property
    def dimensions(self):
        """Get dimensions"""
        return self.__dimensions

    @product_code.setter
    def product_code(self, value):
        """Set product_code"""
        if not isinstance(value, int):
            raise TypeError('Product code must be Integer type!')
        if value <= 0.:
            raise ValueError('Product code cannot be less than or equal to 0')
        self.__product_code = value

    @price.setter
    def price(self, value):
        """Set price"""
        if not isinstance(value, (int, float)):
            raise TypeError('Price must be a number!')
        if value <= 0.:
            raise ValueError('Price cannot be less than or equal to 0')
        self.__price = value

    @description.setter
    def description(self, value):
        """Set description"""
        if not isinstance(value, str):
            raise TypeError('Description must be a string!')
        self.__description = value

    @dimensions.setter
    def dimensions(self, value):
        """Set dimensions"""
        if not isinstance(value, (int, float)):
            raise TypeError('Dimensions must be a number!')
        if value <= 0.:
            raise ValueError('Dimensions cannot be less than or equal to 0')
        self.__dimensions = value

    def __str__(self):
        """Represents the class objects as a string"""
        return f'[{self.product_code}] Price: {self.price}. ' \
               f'Description: {self.description}. Dimensions: {self.dimensions}'
