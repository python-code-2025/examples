from animal import Animal

class Cat(Animal):
    def __init__(self, c, owner):
        self.color=c
        self.__owner=owner

    def getCatInfo(self):
        print(f"The cat of {self.__owner} is {self.color}")

    #destructor
    def __del__(self):
        print("The cat object is deleted")

    def info(self):
        print("This is cat")