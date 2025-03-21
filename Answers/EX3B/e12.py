class ClassA:
    def __init__(self):
        print("ClassA constructor")

class ClassB:
    def __init__(self):
        print("ClassB constructor")

class ClassC(ClassA, ClassB):
    def __init__(self):
        super().__init__()
        ClassB.__init__(self)