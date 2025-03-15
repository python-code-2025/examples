from abc import ABC, abstractmethod

class AnimalAbs(ABC):
    @abstractmethod
    def sound(self):
        pass  # This is an abstract method, no implementation here.