class TaskNode:
    def __init__(self, task):
        self.task = task
        self.next = None

class TaskScheduler:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = TaskNode(task)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f'Task "{task}" added.')

    def remove_task(self, task):
        if not self.head:
            print("Task list is empty.")
            return

        if self.head.task == task:
            self.head = self.head.next
            print(f'Task "{task}" removed.')
            return

        temp = self.head
        while temp.next and temp.next.task != task:
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next
            print(f'Task "{task}" removed.')
        else:
            print(f'Task "{task}" not found.')

    def display_tasks(self):
        if not self.head:
            print("No tasks scheduled.")
            return

        print("Scheduled Tasks:")
        temp = self.head
        while temp:
            print(f"- {temp.task}")
            temp = temp.next

# Example Usage
tasks = TaskScheduler()
tasks.add_task("Complete Python assignment")
tasks.add_task("Prepare for OOP quiz")
tasks.add_task("Attend lab session")

tasks.display_tasks()

tasks.remove_task("Prepare for OOP quiz")
tasks.display_tasks()
