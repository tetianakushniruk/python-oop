from sys import argv
# The operator module supplies functions that are equivalent to Python's operators
# for example, operator.add(a, b) returns a+b, etc.add
from operator import *

operations = ('add', 'sub', 'mul', 'truediv')

if __name__ == '__main__':
    if len(argv) != 4 or argv[1] not in operations or not argv[2].isdigit() or not argv[3].isdigit():
        print('Please enter arguments properly: operation operand operand')
        print('Operations: add, sub, mul, truediv')
    else:
        try:
            print('Result: ', eval(argv[1] + '(' + argv[2] + ', ' + argv[3] + ')'))
        except ZeroDivisionError:
            print("Division by zero")

