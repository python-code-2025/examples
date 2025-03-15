from person18 import Person

# create using full constructor
objectPerson1 = Person("Teppo Testi", 30, "Oulu")
print(objectPerson1)

# create using name constructor
objectPerson2 = Person.name_constructor("Liis Joki")
print(objectPerson2)