from Person import Person
from Notebook import Notebook


if __name__ == '__main__':
    p1 = Person('Tatiana', 'Kushniruk', '+380969874634', '29.03.2003')
    p2 = Person('Brian', 'Molko', '+447911123456', '10.12.1972')
    n1 = Notebook()
    n2 = Notebook([p1, p2])

    # print(n2)
    # print(n2 - p2)
    # print(n2 * '29.03.2003')

    # n3 = n1 + p2
    # print(n3)

    # n1 += p2
    # print(n1)
    # print(n1 * 'Molko')
