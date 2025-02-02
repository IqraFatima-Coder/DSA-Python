class ToDoList:
    def __init__(self):
        self.tasks = []  # List of task names
        self.status = []  # Parallel list for task status (True = Completed, False = Pending)

    def add_task(self, task):
        """Add a new task with default status as False (Pending)."""
        self.tasks.append(task)
        self.status.append(False)

    def mark_completed(self, task):
        """Mark a task as completed if it exists."""
        if task in self.tasks:
            index = self.tasks.index(task)
            self.status[index] = True
            print(f"Task '{task}' marked as completed.")
        else:
            print(f"Task '{task}' not found.")

    def view_completed_tasks(self):
        """Display only completed tasks."""
        print("Completed Tasks:")
        found = False
        for i, (task, done) in enumerate(zip(self.tasks, self.status), 1):
            if done:
                print(f"{i}. {task}")
                found = True
        if not found:
            print("No completed tasks yet.")

    def view_all_tasks(self):
        """Display all tasks with their status."""
        print("All Tasks:")
        for i, (task, done) in enumerate(zip(self.tasks, self.status), 1):
            status_text = "✓ Completed" if done else "✗ Pending"
            print(f"{i}. {task} - {status_text}")

# Testing the To-Do List Enhancement
to_do = ToDoList()
to_do.add_task("Buy groceries")
to_do.add_task("Complete homework")
to_do.mark_completed("Buy groceries")
to_do.view_completed_tasks()
to_do.view_all_tasks()
