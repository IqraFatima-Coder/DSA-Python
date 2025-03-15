class AITaskQueue:
    def __init__(self, gpus):
        self.tasks = []  # Task queue
        self.gpus = gpus  # List of GPUs

    def add_task(self, task):
        """Add an AI task to the queue."""
        self.tasks.append(task)

    def process_tasks(self):
        """Assign tasks to GPUs in round-robin order."""
        if not self.tasks:
            print("No AI tasks in the queue.")
            return
        
        gpu_index = 0  # Track which GPU to assign next
        while self.tasks:
            task = self.tasks.pop(0)  # Get the first task (FIFO order)
            gpu = self.gpus[gpu_index]  # Assign to GPU in round-robin
            print(f"Assigning '{task}' to {gpu}")

            gpu_index = (gpu_index + 1) % len(self.gpus)  # Move to next GPU

# Example Usage
ai_queue = AITaskQueue(["GPU1", "GPU2", "GPU3"])
ai_queue.add_task("AI Model Training")
ai_queue.add_task("Image Processing")
ai_queue.add_task("NLP Processing")
ai_queue.add_task("Autonomous Driving AI")

ai_queue.process_tasks()
