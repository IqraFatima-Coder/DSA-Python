import time

class PrintQueue:
    def __init__(self):
        self.queue = []

    def add_job(self, job):
        self.queue.insert(0, job)

    def process_job(self):
        if self.queue:
            print(f"Printing: {self.queue.pop()}")
            time.sleep(1)
        else:
            print("No print jobs in queue.")

# Example Usage
pq = PrintQueue()
pq.add_job("Document1.pdf")
pq.add_job("Image.png")
pq.process_job()  # Printing: Document1.pdf
