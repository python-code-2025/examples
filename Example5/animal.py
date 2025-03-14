class Animal:
    def __init__(self, c):
        self.color=c

    def getColor(self):
        return self.color
    
    def setColor(self, value):
        self.color=value

    def info(self):
        print("this is animal")