class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
        else:
            print(f"Popped: {self.stack.pop()}")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)


stack = Stack()

while True:
    choice = input("Enter 'push', 'pop', or 'exit': ").strip().lower()
    if choice == 'push':
        item = input("Enter item to push: ")
        stack.push(item)
    elif choice == 'pop':
        stack.pop()
    elif choice == 'exit':
        break
    else:
        print("Invalid choice!")
