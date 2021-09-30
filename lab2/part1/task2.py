import math


class Rational:
    def __init__(self, num=1, den=1):
        if not den:
            raise ZeroDivisionError("Division by zero")
        elif not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Correct type: integer")
        else:
            gcd = math.gcd(num, den)
            self.__num = num // gcd
            self.__den = den // gcd

    def print_fraction(self):
        return str(self.__num) + '/' + str(self.__den)

    def print_float(self):
        return self.__num / self.__den


if __name__ == "__main__":
    x = Rational(2, 4)
    print(x.print_fraction())
    print(x.print_float())
