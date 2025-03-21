from abc import ABC, abstractmethod
import math

# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Subclass Circle that implements the abstract methods
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


# Subclass Rectangle that implements the abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


# Example usage:
circle = Circle(5)
print(f"Circle Area: {circle.area()}")  # Area of the circle
print(f"Circle Perimeter: {circle.perimeter()}")  # Perimeter of the circle

rectangle = Rectangle(4, 6)
print(f"Rectangle Area: {rectangle.area()}")  # Area of the rectangle
print(f"Rectangle Perimeter: {rectangle.perimeter()}")  # Perimeter of the rectangle
