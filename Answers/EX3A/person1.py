class Person:
    def __init__(self, name, age):
        self.__name=name
        self.__age=age
        print(f"Name is {self.__name} and age is {self.__age}")