class Person:
    #full details constructor
    def __init__(self, name, age=None, city=None):
        self.name = name
        self.age = age
        self.city = city

    @classmethod
    #just the name
    def name_constructor(cls, name):
        return cls(name) 

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age if self.age is not None else 'Unknown'}, City: {self.city if self.city else 'Unknown'}"


