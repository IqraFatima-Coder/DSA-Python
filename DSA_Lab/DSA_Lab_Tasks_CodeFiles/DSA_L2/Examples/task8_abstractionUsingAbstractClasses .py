from abc import ABC, abstractmethod 
class Shape(ABC): 
 @abstractmethod 
 def area(self): 
  pass 
 @abstractmethod 
 def perimeter(self): 
  pass 
 
class Rectangle(Shape): 
 def __init__(self, length, width): 
  self.length = length
  self.width = width 
 def area(self): 
  return self.length * self.width 
 def perimeter(self): 
  return 2 * (self.length + self.width) 
 
rect = Rectangle(10, 5) 
print("Area:", rect.area()) 
print("Perimeter:", rect.perimeter()) 