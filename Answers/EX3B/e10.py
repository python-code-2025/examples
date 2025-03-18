from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing Machine turned on")