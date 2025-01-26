#Using Python Math Library Create a program to find the greatest common divisor (GCD) 
#and least common multiple (LCM) of two numbers using the math module. 
#o Input: 12, 15 
#o Output: 
#makefile 
#CopyEdit 
#GCD: 3   
#LCM: 60 
import math
def find_gcd_lcm(num1, num2):
    # Calculate GCD using math.gcd()
    gcd = math.gcd(num1, num2)
    # Calculate LCM using the formula: LCM = (num1 * num2) // GCD
    lcm = (num1 * num2) // gcd
    return gcd, lcm
# Input numbers
num1 = 12
num2 = 15
# Find GCD and LCM
gcd, lcm = find_gcd_lcm(num1, num2)
# Print the results
print("GCD:", gcd)  # Output: GCD: 3
print("LCM:", lcm)  # Output: LCM: 60
