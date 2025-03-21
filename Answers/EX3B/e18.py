class Worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        # Worker’s method to return the salary
        return f"Worker {self.name}'s salary is {self.salary}"

class Engineer:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        # Engineer’s method to return the salary
        return f"Engineer {self.name}'s salary is {self.salary}"

# SoftwareEngineer class inherits from both Worker and Engineer
class SoftwareEngineer(Worker, Engineer):
    def __init__(self, name, salary):
        # Calling the __init__ methods of both Worker and Engineer
        Worker.__init__(self, name, salary)
        Engineer.__init__(self, name, salary)

    def get_salary(self):
        # Calls both get_salary methods from Worker and Engineer
        worker_salary = Worker.get_salary(self)
        engineer_salary = Engineer.get_salary(self)
        return f"{worker_salary} and {engineer_salary}"

# Example usage:
software_engineer = SoftwareEngineer("Alice", 80000)
print(software_engineer.get_salary())  # Using both methods
