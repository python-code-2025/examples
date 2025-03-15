from dog10 import Dog
from cat10 import Cat

objectDog=Dog()
objectCat=Cat()
objectDog.sound()
objectCat.sound()

#if you try this, you will get an error
#from animalabs import AnimalAbs
#objectAnimalAbs=AnimalAbs()

#the error message is 
#TypeError: Can't instantiate abstract class AnimalAbs without an implementation for abstract method 'sound'