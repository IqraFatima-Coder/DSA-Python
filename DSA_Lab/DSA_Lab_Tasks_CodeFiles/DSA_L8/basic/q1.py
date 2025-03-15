class ListQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        """Add an item to the queue (end of list)."""
        self.items.insert(0, data)

    def dequeue(self):
        """Remove and return the first item from the queue."""
        if self.is_empty():
            return "Queue is empty!"
        return self.items.pop()

    def peek(self):
        """Return the front element without removing it."""
        return self.items[-1] if not self.is_empty() else "Queue is empty!"

    def size(self):
        """Return the size of the queue."""
        return len(self.items)

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

# Example Usage
queue = ListQueue()
queue.enqueue("Task 1")
queue.enqueue("Task 2")
print("First item:", queue.peek())  # Task 1
print("Dequeued:", queue.dequeue())  # Task 1
print("Queue size:", queue.size())  # 1
