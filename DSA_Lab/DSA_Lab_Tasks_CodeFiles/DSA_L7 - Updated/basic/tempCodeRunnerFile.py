def peek(stack):
    if stack:
        return stack[-1]
    return None  # If stack is empty

stack = [10, 20, 30]
print("Top element:", peek(stack))  # Output: 30
