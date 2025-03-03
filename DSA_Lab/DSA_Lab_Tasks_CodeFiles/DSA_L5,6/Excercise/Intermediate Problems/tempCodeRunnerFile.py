class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class TaskScheduler:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def execute_tasks(self, cycles=2):
        if not self.head:
            print("No tasks to execute.")
            return
        temp = self.head
        for _ in range(cycles):
            print(f"Executing: {temp.task}")
            temp = temp.next
        print("(Tasks repeated)")

# Usage
scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")
scheduler.execute_tasks()
