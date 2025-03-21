class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def __str__(self):
        return f"Employee: {self.name}, Position: {self.position}"
    
objectEmployee=Employee("Teppo Testi","Director")
print(objectEmployee)