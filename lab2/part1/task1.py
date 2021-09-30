class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Correct types: int, float")
        elif value <= 0. or value > 20.:
            raise ValueError("0 < length < 20")
        else:
            self.__length = value

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Correct types: int, float")
        elif value <= 0. or value > 20.:
            raise ValueError("0 < length < 20")
        else:
            self.__width = value

    def perimeter(self):
        return (self.__length + self.__width) * 2

    def area(self):
        return self.__length * self.__width


if __name__ == "__main__":
    rec = Rectangle()
    rec.length = 2
    rec.width = 6
    print(str(rec.length) + ' ' + str(rec.width))
    print(rec.perimeter())
    print(rec.area())
