from person12 import Person

class Student(Person):

    def __init__(self, name, age,grade):
        super().__init__(name, age)
        self.__grade=grade

    def getStudentData(self):
        print(f"Name= {self._name}")
        print(f"Age= {self._age}")
        print(f"Grade= {self.__grade}")