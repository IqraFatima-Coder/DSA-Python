class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top is None:
            print("Stack Underflow: No elements to pop!")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data
    
    def peek(self):
        return self.top.data if self.top else None
    
    def isEmpty(self):
        return self.top is None
    
    def display(self):
        current = self.top
        print("Stack:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example Usage
stack = StackLinkedList()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.pop()
stack.display()
