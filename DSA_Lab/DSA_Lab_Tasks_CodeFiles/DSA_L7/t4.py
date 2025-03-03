'''4. Design a Special Stack with Two Stacks 
Problem Statement: 
Design a stack that supports the following operations in O(1) time: 
1. push(x): Push an element onto the stack. 
2. pop(): Remove the top element. 
3. get_min(): Get the minimum element in the stack. 
4. get_max(): Get the maximum element in the stack. 
 
Example: 
Input: 
s = SpecialStack() 
s.push(5) 
s.push(1) 
s.push(3) 
Output: 
print(s.get_min())  # 1 
print(s.get_max())  # 5 
Hints: Use two stacks: main_stack for storing elements and min_stack/max_stack for 
tracking min/max values.'''
class SpecialStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        self.max_stack = []
    def push(self, x):
        self.main_stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
    def pop(self):

        if self.main_stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        if self.main_stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        return self.main_stack.pop()
    def get_min(self):
        return self.min_stack[-1]
    
    def get_max(self):
        return self.max_stack[-1]
    
s = SpecialStack()
s.push(5)
s.push(1)
s.push(3)
print(s.get_min())  # 1
print(s.get_max())  # 5
# Time Complexity: O(1) for all operations
# Space Complexity: O(n) for n elements in the stack
# Output: 1
# 5
# Explanation: The minimum element in the stack is 1 and the maximum element in the stack is 5.
# Both of these operations are performed in O(1) time complexity.
# The push and pop operations are also performed in O(1) time complexity.
# Hence, the SpecialStack class is designed

    