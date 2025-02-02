class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print(f"Task '{task}' not found.")

    def view_tasks(self):
        print("Tasks:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

to_do = ToDoList()
to_do.add_task("Buy groceries")
to_do.add_task("Complete homework")
to_do.view_tasks()
to_do.remove_task("Buy groceries")
to_do.view_tasks()
