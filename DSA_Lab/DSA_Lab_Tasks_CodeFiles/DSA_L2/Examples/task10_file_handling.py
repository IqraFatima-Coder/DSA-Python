# Write to a file 
with open("example.txt", "w") as file: 
 file.write("Hello, Python file handling!") 
# Read the file 
with open("example.txt", "r") as file: 
 content = file.read() 
print("File content:", content) 
# Append to the file 
with open("example.txt", "a") as file: 
 file.write("\nAdding a new line.") 
# Delete the file 
import os 
os.remove("example.txt")