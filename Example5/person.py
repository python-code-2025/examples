class Person:
    def __init__(self, name, age):
        self.__name=name
        self.__age=age
        print(f"I am {self.__name} I am {self.__age} years old")