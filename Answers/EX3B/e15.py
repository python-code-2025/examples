class Person:
    population = 0
    
    def __init__(self):
        self.update_population()

    def update_population(self):
        Person.population +=1 #you can not use self.population here

    def get_population(self):
        return Person.population
    
#testing the class
objectPerson1=Person()
print(objectPerson1.get_population())

objectPerson2=Person()
print(objectPerson2.get_population())
print(objectPerson1.get_population())
