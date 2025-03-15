def is_empty(stack):
    return len(stack) == 0

stack = []
print("Stack is empty:", is_empty(stack))  # True
stack.append(5)
print("Stack is empty:", is_empty(stack))  # False
