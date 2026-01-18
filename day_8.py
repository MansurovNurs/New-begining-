class Figure:
    unit = "mm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        print(f'Square side length: {self.__side_length}{self.unit}, area: {self.calculate_area()}{self.unit}')


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        print(f'Rectangle length: {self.__length}{self.unit}, Rectangle width: {self.__width}{self.unit}, area: {self.calculate_area()}{self.unit}')


square1 = Square(15)
square2 = Square(30)

reqtangle1 = Rectangle(12, 25)
reqtangle2 = Rectangle(12, 25)
reqtangle3 = Rectangle(12, 25)

squares = [square1, square2]
rectangles = [reqtangle1, reqtangle2, reqtangle3]

for square in squares:
    print(square.info())

for i in rectangles:
    print(i.info())

