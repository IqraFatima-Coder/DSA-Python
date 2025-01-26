class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")
# Input
name = input("Enter name: ")
salary = input("Enter salary: ")
department = input("Enter department: ")
# Create a Manager object and display details
manager = Manager(name, salary, department)
manager.display_details()
