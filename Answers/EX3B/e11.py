class Student:
    def get_details(self):
        print("Student details")

class Employee:
    def get_details(self):
        print("Employee details")

class GraduateStudent(Student, Employee):
    def show_details(self):
        Student.get_details(self)
        Employee.get_details(self)