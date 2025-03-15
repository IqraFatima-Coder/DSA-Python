#Task 1: Implementing a Stack using Arrays
class StackArray:
    def __init__(self, size):
        self.stack = []
        self.size = size
    
    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)
        else:
            print("Stack Overflow: Cannot add more elements!")
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack Underflow: No elements to pop!")
            return None
    
    def peek(self):
        return self.stack[-1] if self.stack else None
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def display(self):
        print("Stack:", self.stack)

# Example Usage
stack = StackArray(5)
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.pop()
stack.display()
