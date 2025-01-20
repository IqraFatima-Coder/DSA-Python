#Author: Iqra Fatima
#Reg. Number: 23-CP-62
#Task 15: Python Lambda Functions
# Lambda to find square of a number
square = lambda x: x ** 2
print("Square of 5:", square(5))
# Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)
