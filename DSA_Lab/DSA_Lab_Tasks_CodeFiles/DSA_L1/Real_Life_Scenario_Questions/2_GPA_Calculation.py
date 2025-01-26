# 2- GPA Calculation
# Write a program to calculate the GPA of a student.
# Input the grades for 5 courses (on a scale of 4.0) and calculate the average GPA.

# Input the grades for 5 courses
g1 = float(input("Enter your grade points in subject 1: "))
g2 = float(input("Enter your grade points in subject 2: "))
g3 = float(input("Enter your grade points in subject 3: "))
g4 = float(input("Enter your grade points in subject 4: "))
g5 = float(input("Enter your grade points in subject 5: "))

# Calculate the average GPA
average_gpa = (g1 + g2 + g3 + g4 + g5) / 5

# Print the average GPA
print("Your average GPA is:", average_gpa)