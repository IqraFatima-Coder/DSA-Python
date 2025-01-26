#Question3
#Write a program to input three numbers 
#and print the largest one.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
#Now, we'll use if-elif-else statement to find the largest number
if a > b and a > c:
    print("The largest number is", a)
elif b>c:
    print("The largest number is", b)
else:
    print("The largest number is", c)
