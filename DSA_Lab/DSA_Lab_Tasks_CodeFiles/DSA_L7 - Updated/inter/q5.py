def traverse(stack):
    if stack:
        print(stack.pop(), end=" ")
        traverse(stack)

stack = [1, 2, 3, 4, 5]
traverse(stack)
