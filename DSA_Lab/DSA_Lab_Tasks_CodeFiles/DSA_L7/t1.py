'''Problem Statement: 
You are given an array heights[] of size n, where each element represents the height of a bar 
in a histogram. Each bar has a width of 1. Find the largest rectangular area that can be 
formed in the histogram. 
Example: 
Input: 
heights = [2, 1, 5, 6, 2, 3] 
Output: 
10 
Explanation: 
The largest rectangle is formed by heights [5, 6] (from index 2 to 3) with a width of 2 and a 
height of 5, so the area is 5 * 2 = 10. 
Hints: Use a monotonic increasing stack to keep track of indices and calculate the max area.'''
heights = [2, 1, 5, 6, 2, 3]
stack = []
max_area = 0
for i in range(len(heights)):
    while stack and heights[i] < heights[stack[-1]]:
        height = heights[stack.pop()]
        width = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, height * width)
    stack.append(i)
while stack:
    height = heights[stack.pop()]
    width = len(heights) if not stack else len(heights) - stack[-1] - 1
    max_area = max(max_area, height * width)
print(max_area)
# Output
# 10
# Time Complexity: O(n)
# Space Complexity: O(n)