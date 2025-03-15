from shape9 import Shape
from math import pi
class Circle(Shape):
    def __init__(self, radius):
        self.__radius=radius

    def area(self):
        #two decimals to the area
        return round(self.__radius*self.__radius*pi,2)
        