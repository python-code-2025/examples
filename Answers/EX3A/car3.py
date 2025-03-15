class Car:
    def __init__(self,make,model):
        self.__make=make
        self.__model=model

    def getMake(self):
        return self.__make
    
    def getModel(self):
        return self.__model
#ex3 the destructor
    def __del__(self):
        print("car object deleted")


    @classmethod
    def update_class_variable(cls, value):
        cls.class_variable = value
        print(f"Class variable updated to {cls.class_variable}")