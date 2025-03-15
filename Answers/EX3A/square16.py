from shape16 import Shape

class Square(Shape):
    def __init__(self, side):
        self.__side=side

    def area(self):
        return self.__side * self.__side