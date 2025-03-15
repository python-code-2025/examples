from shape9 import Shape
class Rectangle(Shape):
    def __init__(self, width, length):
        self.__width=width
        self.__length=length

    def area(self):
        return self.__width*self.__length
