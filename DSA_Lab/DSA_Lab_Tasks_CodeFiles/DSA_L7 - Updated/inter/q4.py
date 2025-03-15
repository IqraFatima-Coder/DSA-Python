def sorted_insert(stack, element):
    if not stack or element > stack[-1]:
        stack.append(element)
    else:
        temp = stack.pop()
        sorted_insert(stack, element)
        stack.append(temp)

def sort_stack(stack):
    if stack:
        temp = stack.pop()
        sort_stack(stack)
        sorted_insert(stack, temp)

stack = [3, 1, 4, 2]
sort_stack(stack)
print(stack)  # Output: [1, 2, 3, 4]
