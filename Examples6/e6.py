class Dog:
    #constructor1
    def __init__(self, name="none"):
        self.__name=name
        print("object created")

    #constructor2
    @classmethod
    def adog(cls):
        return cls() 
        
    def setName(self, value):
        self.__name=value
    def getName(self):
        return self.__name

#We can create an object like this
objectDog1=Dog("Musti")
#And also we can create object like this
objectDog2=Dog.adog()

objectDog2.setName("Vahti")
print(f"Name of the dog1 is {objectDog1.getName()}")
print(f"Name of the dog2 is {objectDog2.getName()}")