from animal8 import Animal

class Penguin(Animal):

    def sound(self):
        print("This is Penguin")

    #this will call the sound()-method if the base class
    def animal_sound(self):
        super().sound()