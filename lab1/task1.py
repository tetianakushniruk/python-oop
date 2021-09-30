# The sys module provides access to some variables and
# functions that interact strongly the interpreter
# The argv method returns the string arguments
# passed to the Python script as a list
from sys import argv

if __name__ == '__main__':
    # The eval() method parses the expression passed to
    # this method and runs python expression (code) within the program
    if len(argv) != 4 or not argv[1].isdigit() or argv[2] not in '+-*/' or not argv[3].isdigit():
        print('Please enter arguments properly: operand operator operand')
    else:
        try:
            print('Result: ', eval(argv[1] + argv[2] + argv[3]))
        except ZeroDivisionError:
            print("Division by zero")
