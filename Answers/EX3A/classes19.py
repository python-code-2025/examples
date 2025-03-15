#This time I added all classes in the same file
#it is not a good solution, but it is possible

class ClassA:
    def method(self):
        return "Method from ClassA"

class ClassB:
    def method(self):
        return "Method from ClassB"

class ClassC(ClassA, ClassB):
    def method(self):
        return "Method from ClassC"
    
