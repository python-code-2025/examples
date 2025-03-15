from shape16 import Shape
from math import pi

class Circle(Shape):
    def __init__(self, radius):
        self.__radius=radius

    def area(self):
        return round(self.__radius * self.__radius * pi,2)