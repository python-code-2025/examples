class Car:
    def __init__(self, model):
        self.__model = model
        self.is_running = False  # A flag to track whether the car is started

    def start(self):
        # Start the car
        self.is_running = True
        print(f"{self.__model} is now running.")
        
        # Trigger the start of the other car
        print(f"Triggering the start of the other car...")
        self.trigger_other_car_start()

    def trigger_other_car_start(self):
        # Here we manually call the start method of the other car instance
        print(f"The other car is now started by {self.__model}!")
        
        # Assuming the method is being called from car1 to trigger car2, 
        # we explicitly call start on car2 here.
        if self.__model == "Car1":
            car2.start()  # Explicitly calling car2.start()

# Instantiate two Car objects
car1 = Car("Car1")
car2 = Car("Car2")

# Call start from car1 to trigger car2's start
car1.start()

#check if the car is running
print(f"car1 is_running={car1.is_running}")
print(f"car2 is_running={car2.is_running}")


