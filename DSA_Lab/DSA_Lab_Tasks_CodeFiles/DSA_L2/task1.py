import array 
# Create an array of integers 
numbers = array.array('i', [1, 2, 3, 4, 5]) 
# Access and modify array elements 
print("Original array:", numbers) 
numbers[1] = 10 
print("Modified array:", numbers) 
# Add and remove elements 
numbers.append(6) 
numbers.pop(0) 
print("Updated array:", numbers)