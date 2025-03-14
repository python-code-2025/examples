from animal import Animal
class Dog(Animal):
    def __init__(self, c,city):
        super().__init__(c)
        self.city=city

    def dogInfo(self):
        print(f"The {self.color} dog lives in {self.city}")