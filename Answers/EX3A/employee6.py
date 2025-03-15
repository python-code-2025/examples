class Employee:
    def __init__(self, name, age, position):
        self.__name = name
        self.__age = age
        self.__position = position

    @classmethod
    def create_employee(cls, name, age, position):
        return cls(name, age, position)
    
    #you can define what the print(object) shows with below code
    def __str__(self):
        return f"Object-Employee(Name: {self.__name}, Age: {self.__age}, Position: {self.__position})"