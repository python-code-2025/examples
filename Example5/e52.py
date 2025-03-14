from cat import Cat
from dog import Dog

objectCat1=Cat("orange","Teppo Testi")
objectDog1=Dog("gray","Oulu")


print(f"The color of the cat ={objectCat1.getColor()}")
print(f"The color of the dog ={objectDog1.getColor()}")

objectCat1.getCatInfo()
#We can not reach private variables (name starts with __)
#print(f"Private Variable: {objectCat1.__owner}")
print(f"Public Variable: {objectCat1.color}")

#the objects wwill be deleted automatically in Python 
#so you don't need to delete tjem like below
del objectCat1
objectDog1.dogInfo()