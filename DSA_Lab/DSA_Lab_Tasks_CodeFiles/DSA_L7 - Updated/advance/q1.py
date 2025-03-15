def call_stack_simulation(n):
    stack = []
    while n > 0:
        stack.append(n)
        n -= 1
    while stack:
        print(f"Returning from function({stack.pop()})")

call_stack_simulation(5)
