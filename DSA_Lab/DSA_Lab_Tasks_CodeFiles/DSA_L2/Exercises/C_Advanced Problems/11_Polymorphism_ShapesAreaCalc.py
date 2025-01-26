import math
class Shape:
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius ** 2
# Input
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
radius = float(input("Enter radius of circle: "))
rect = Rectangle(length, width)
circle = Circle(radius)
# Output
print("Rectangle Area:", rect.calculate_area())  # Output: 15
print("Circle Area:", round(circle.calculate_area(), 2))  # Output: 50.24
