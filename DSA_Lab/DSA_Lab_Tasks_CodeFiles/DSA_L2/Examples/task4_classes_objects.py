class Student: 
 def __init__(self, name, age): 
  self.name = name 
  self.age = age 
 def display_info(self): 
  print(f"Student Name: {self.name}, Age: {self.age}")
# Create an object of the Student class 
student1 = Student("Alice", 20) 
student1.display_info()