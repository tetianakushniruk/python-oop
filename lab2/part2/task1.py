from Product import Product
from Customer import Customer
from Order import Order


if __name__ == '__main__':
    product1 = Product(253, 250, 'Phone', 350)
    product2 = Product(296, 524, 'Laptop', 1596)
    customer1 = Customer('Kushniruk', 'Tatiana', 'Alexandrovna', '+380(96)-987-46-34')
    order1 = Order({product1: 2, product2: 5}, customer1)
    product3 = Product(532, 1296, 'Macbook', 1299)
    order1.add_product(product3, 1)
    order1.change_quantity(296, 10)
    print(order1)
