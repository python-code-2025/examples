from student7 import Student

objStudent=Student()

print(f"name of the school is {objStudent.get_school_name()}")

#calling the setter was not mentioned 
#but I added it here

objStudent.set_school_name("Lyseon lukio")
print(f"name of the school is {objStudent.get_school_name()}")
