#1. Array Rotation Write a Python program to rotate an array by a given number of 
#steps. 
#o Input: [1, 2, 3, 4, 5], Steps: 2 
#o Output: [4, 5, 1, 2, 3] 
n=int(input("Enter the number of elements in the array: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the element: ")))
steps=int(input("Enter the number of steps to rotate the array: "))
print("Original array:",arr)
for i in range(steps):
    arr.insert(0,arr.pop())
print("Rotated array:",arr)