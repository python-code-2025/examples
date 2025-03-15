class Car:
    def __init__(self,make,model):
        self.__make=make
        self.__model=model

    def getMake(self):
        return self.__make
    
    def getModel(self):
        return self.__model