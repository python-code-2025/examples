class Parent:
    def __init__(self, name):
        self.__name=name 

    #protected method
    def _getParentData(self):
        print(f"Name = {self.__name}")

    def getInfo(self):
        print(f"This is public")

