import heapq

class ProcessQueue:
    def __init__(self):
        self.queue = []

    def add_process(self, priority, process_name):
        """Add a process with a priority (lower number = higher priority)."""
        heapq.heappush(self.queue, (priority, process_name))

    def execute_process(self):
        """Execute the highest priority process."""
        if not self.queue:
            return "No processes to execute."
        return f"Executing: {heapq.heappop(self.queue)[1]}"

# Example Usage
pq = ProcessQueue()
pq.add_process(3, "Process C")
pq.add_process(1, "Process A")  # Highest priority
pq.add_process(2, "Process B")
print(pq.execute_process())  # Executing: Process A
