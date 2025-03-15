class Student:
    #private variable
    __school_name="My School"

    #getter method
    def get_school_name(self):
        return self.__school_name 
    
    #setter method was not mentioned in the exercise 
    #but I added it also
    def set_school_name(self, name):
        self.__school_name=name