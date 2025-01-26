#Question 10: Find Prime Numbers in a Range
#Write a program to print all prime numbers between 1 and 50.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(1, 51):
    if is_prime(num):
        print(num)