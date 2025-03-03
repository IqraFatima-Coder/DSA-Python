class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.stack = [None] * capacity
    
    def push(self, item):
        if self.is_full():
            print("Stack overflow!")
            return
        self.top += 1
        self.stack[self.top] = item
    
    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item
        
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.top]
    
    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

# Example Usage
stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.peek())
print(stack.is_empty())
print(stack.is_full())