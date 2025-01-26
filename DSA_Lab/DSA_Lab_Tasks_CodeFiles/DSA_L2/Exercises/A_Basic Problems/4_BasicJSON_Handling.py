# Basic JSON Handling Write a program to create a JSON object with keys name, age, 
#and grade. Then read and print the values. 
#o Input: { "name": "Alice", "age": 20, "grade": "A" } 
#o Output:
#makefile 
#CopyEdit 
#ame: Alice   
#Age: 20   
#Grade: A 

import json
json_data = '{"name": "Alice", "age": 20, "grade": "A"}'
# Convert JSON data to Python dictionary
data = json.loads(json_data)
# Print the values
print("Name:", data["name"])  # Output: Name: Alice
print("Age:", data["age"])    # Output: Age: 20
print("Grade:", data["grade"]) # Output: Grade: A
