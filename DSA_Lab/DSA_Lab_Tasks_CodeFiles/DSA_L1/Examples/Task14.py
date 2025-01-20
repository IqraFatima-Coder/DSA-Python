#Author: Iqra Fatima
#Reg. Number: 23-CP-62
#Task 14: Python Functions
#Program 1
# Define a function to greet the user
def greet(name):
    print(f"Hello, {name}! Welcome to Python programming.")
# Call the function
greet("Alice")
greet("Bob")
#Program 2
#Define a function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Input from user
num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
