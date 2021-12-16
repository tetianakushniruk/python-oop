import math


class Rational:
    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.reduction()

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, int):
            raise TypeError("Correct type: integer")
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if not value:
            raise ZeroDivisionError("Division by zero")
        if not isinstance(value, int):
            raise TypeError("Correct type: integer")
        self.__denominator = value

    def reduction(self):
        if self.numerator < 0 and self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // gcd
        self.denominator = self.denominator // gcd

    def __add__(self, other):
        if isinstance(other, int):
            return Rational(self.numerator + other * self.denominator, self.denominator)
        elif isinstance(other, Rational):
            return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                            self.denominator * other.denominator)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, int):
            self.numerator += other * self.denominator
        elif isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
            self.denominator *= other.denominator
        else:
            return NotImplemented
        self.reduction()
        return self

    def __sub__(self, other):
        if isinstance(other, int):
            return Rational(self.numerator - other * self.denominator, self.denominator)
        elif isinstance(other, Rational):
            return Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                            self.denominator * other.denominator)
        else:
            return NotImplemented

    def __isub__(self, other):
        if isinstance(other, int):
            self.numerator -= other * self.denominator
        elif isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
            self.denominator *= other.denominator
        else:
            return NotImplemented
        self.reduction()
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            return Rational(self.numerator * other, self.denominator)
        elif isinstance(other, Rational):
            return Rational(self.numerator * other.numerator, self.denominator * other.denominator)
        else:
            return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            self.numerator *= other
        elif isinstance(other, Rational):
            self.numerator *= other.numerator
            self.denominator *= other.denominator
        else:
            return NotImplemented
        self.reduction()
        return self

    def __truediv__(self, other):
        if isinstance(other, int):
            return Rational(self.numerator, self.denominator * other)
        elif isinstance(other, Rational):
            return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
        else:
            return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, int):
            self.denominator *= other
        elif isinstance(other, Rational):
            self.numerator *= other.denominator
            self.denominator *= other.numerator
        else:
            return NotImplemented
        self.reduction()
        return self

    def __lt__(self, other):
        if isinstance(other, int):
            return self.numerator < other * self.denominator
        elif isinstance(other, Rational):
            return self.numerator * other.denominator < other.numerator * self.denominator
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, int):
            return self.numerator <= other * self.denominator
        elif isinstance(other, Rational):
            return self.numerator * other.denominator <= other.numerator * self.denominator
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, int):
            return self.numerator > other * self.denominator
        elif isinstance(other, Rational):
            return self.numerator * other.denominator > other.numerator * self.denominator
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, int):
            return self.numerator >= other * self.denominator
        elif isinstance(other, Rational):
            return self.numerator * other.denominator >= other.numerator * self.denominator
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, int):
            return self.numerator == other * self.denominator
        elif isinstance(other, Rational):
            return self.numerator * other.denominator == other.numerator * self.denominator
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, int):
            return self.numerator != other * self.denominator
        elif isinstance(other, Rational):
            return self.numerator * other.denominator != other.numerator * self.denominator
        else:
            return NotImplemented

    def print_fraction(self):
        if self.denominator == 1:
            return str(self.numerator)
        return str(self.numerator) + '/' + str(self.denominator)

    def print_float(self):
        return self.numerator / self.denominator

