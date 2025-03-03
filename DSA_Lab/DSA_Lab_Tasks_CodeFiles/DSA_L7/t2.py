'''2. Trapping Rainwater Problem 
Problem Statement: 
Given an array heights[] of size n, where heights[i] represents the height of the building at 
index i, determine the amount of rainwater trapped between the buildings after rainfall. 
Example: 
Input: 
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] 
Output: 
6 
Explanation: 
Water is trapped at indices 2, 4, 5, 6, 9, 10 with units [1, 1, 2, 1, 1, 1], totaling 6 units. 
Hints: Use a monotonic decreasing stack or track left max and right max heights.'''
def trap(height):
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = height[0]
    right_max[n - 1] = height[n - 1]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]
    return water
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(heights))
# Output
# 6
# Explanation:
# Water is trapped at indices 2, 4, 5, 6, 9, 10 with units [1, 1, 2, 1, 1, 1], totaling 6 units.
# Time Complexity: O(n)
# Space Complexity: O(n)