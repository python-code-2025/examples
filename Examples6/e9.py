class Person:
    def __init__(self,fname):
        self.__fname=fname

    @property
    def _fname(self):
        return self.__fname

    @_fname.setter
    def _fname(self, value):
        self.__fname = value

    #set the return for print(object)
    def __str__(self):
        return f"the fname of the object = {self.__fname}"

objectPerson=Person("Ville")
#_fname is a property and we can use it like this
print(objectPerson._fname)
objectPerson._fname = "Jussi" 
print(objectPerson._fname)

print(objectPerson)

