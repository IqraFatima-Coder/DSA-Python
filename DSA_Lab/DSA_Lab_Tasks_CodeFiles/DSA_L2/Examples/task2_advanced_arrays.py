import array 
# Create an array of integers 
numbers = array.array('i', [5, 3, 8, 6, 2]) 
# Reverse the array 
numbers.reverse() 
print("Reversed array:", numbers) 
# Sort the array (manual sorting) 
for i in range(len(numbers)): 
 for j in range(i + 1, len(numbers)): 
   if numbers[i] > numbers[j]: 
     numbers[i], numbers[j] = numbers[j], numbers[i] 
print("Manually sorted array:", numbers) 
# Find the maximum and minimum values
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers)) 
# Count occurrences of an element 
numbers.append(5) 
print("Occurrences of 5:", numbers.count(5))