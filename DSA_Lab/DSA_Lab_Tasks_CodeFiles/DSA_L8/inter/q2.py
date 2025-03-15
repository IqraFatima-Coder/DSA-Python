def round_robin(tasks, quantum):
    queue = tasks[:]
    while queue:
        task, time = queue.pop(0)
        if time > quantum:
            print(f"Processing {task} for {quantum}ms, remaining {time - quantum}ms")
            queue.append((task, time - quantum))
        else:
            print(f"Completed {task} in {time}ms")

# Example Usage
tasks = [("Task A", 5), ("Task B", 10)]
round_robin(tasks, 4)
