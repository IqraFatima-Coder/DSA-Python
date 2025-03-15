class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.insert(0, task)

    def complete_task(self):
        if self.tasks:
            return f"Completed: {self.tasks.pop()}"
        return "No tasks remaining."

    def view_tasks(self):
        return self.tasks[::-1]

# Example Usage
tm = TaskManager()
tm.add_task("Task 1")
tm.add_task("Task 2")
print("Tasks:", tm.view_tasks())  # ['Task 1', 'Task 2']
print(tm.complete_task())  # Completed: Task 1
