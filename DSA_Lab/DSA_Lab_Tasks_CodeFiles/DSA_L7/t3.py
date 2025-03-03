'''3. Find Celebrity in a Party (Stack Approach) 
Problem Statement: 
You are given n people at a party, labeled as 0 to n-1. A celebrity is a person who: 
1. Knows nobody at the party. 
2. Is known by everyone at the party. 
You are given a function knows(a, b) which returns True if a knows b, and False otherwise. 
Find the celebrity in O(n) time complexity using a stack. 
Example: 
Input (Matrix Representation of knows(a, b)): 
M = [[0, 1, 1], [0, 0, 1], [0, 0, 0]] 
Output: 
2 
Explanation: 
Person 2 is known by everyone (0 and 1) and does not know anyone, so 2 is the celebrity. 
Hints: Use a stack to eliminate non-celebrities and verify the last candidate. '''
def knows(a, b):
    M = [[0, 1, 1], [0, 0, 1], [0, 0, 0]]
    return M[a][b]
def find_celebrity(n, knows):
    stack = list(range(n))
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        if knows(a, b):
            stack.append(b)
        else:
            stack.append(a)
    candidate = stack.pop()
    for i in range(n):
        if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
            return -1
    return candidate
n = 3
print(find_celebrity(n, knows))
# Output
# 2
