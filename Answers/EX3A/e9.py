from circle9 import Circle
from rectangle9 import Rectangle

objCircle=Circle(10)
objRectangle=Rectangle(2,4)

print(f"Area of the Circle is {objCircle.area()}")

print(f"Area of the Rectangle is {objRectangle.area()}")

#polymorfism 
# Creating an empty list to store objects
object_list = []

# Adding objects to the list
object_list.append(objCircle)
object_list.append(objRectangle)

# Printing the object areas from the list
print("OBJECT LIST:")
for obj in object_list:
    print(f"Area of the object is {obj.area()}")