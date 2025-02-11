class ToDoList:
    def __init__(self):
        self.tasks=[]
        self.status=[]
    def add_task(self, task):
        self.tasks.append(task)
        self.status.append("Not Completed")
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.status[i].remove()
        else:
            print(f"Task '{task}' not found.")

    def view_tasks(self):
        print("Tasks:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def change_status(self,i):
        if i in range(1,len(self.tasks)+1):
            if self.status[i-1]=="Not Completed":
                self.status[i-1]="Completed"
            else:
                self.status[i-1]="Not Completed"
        else:
            print("Invalid Task Number")
             
    
    
to_do = ToDoList()


 