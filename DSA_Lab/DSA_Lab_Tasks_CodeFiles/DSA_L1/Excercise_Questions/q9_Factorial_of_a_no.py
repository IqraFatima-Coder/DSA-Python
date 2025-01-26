#Question 9: Calculate the Factorial of a Number
#Write a program to calculate the factorial of a
# number using a loop.
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
n = int(input("Enter a number: "))
print("Factorial of",n,"is",factorial(n))

