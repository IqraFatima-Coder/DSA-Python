#Write a program to print the multiplication 
#table for a given number (from 1 to 10).
n= int(input("Enter a number:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    