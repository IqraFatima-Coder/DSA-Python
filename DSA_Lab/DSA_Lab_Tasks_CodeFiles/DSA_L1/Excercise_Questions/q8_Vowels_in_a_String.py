#Write a program to count
# the number of vowels in a string the user provides.
str = input("Enter a string: ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
count = 0
for i in str:
    if i in vowels:
        count+=1
print("Number of vowels in the string:",count)
