from parent13 import Parent
class Child(Parent):
    def __init__(self, name, color):
        super().__init__(name)  # Call Parent class constructor
        self.__color = color
    
    def getChildData(self):
        super()._getParentData()
        print(f"Color: {self.__color}")