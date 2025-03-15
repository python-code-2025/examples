from vehicle2 import Vehicle
from car2 import Car

objectVehicle=Vehicle()

testing1=isinstance(objectVehicle,Vehicle)

print(testing1)

#another test
objectCar=Car('Volvo','V70')
testing2=isinstance(objectCar,Vehicle)

print(testing2)
