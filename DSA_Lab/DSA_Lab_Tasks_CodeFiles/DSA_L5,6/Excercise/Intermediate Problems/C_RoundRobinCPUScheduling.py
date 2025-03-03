class Node:
    def __init__(self, process, time):
        self.process = process
        self.time = time
        self.next = None

class CPU_Scheduler:
    def __init__(self):
        self.head = None

    def add_process(self, process, time):
        new_node = Node(process, time)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def execute(self, quantum=3):
        if not self.head:
            print("No processes to execute.")
            return
        temp = self.head
        while True:
            if temp.time > 0:
                execute_time = min(temp.time, quantum)
                temp.time -= execute_time
                print(f"Executing {temp.process} for {execute_time} units")
                if temp.time == 0:
                    print(f"{temp.process} completed.")
            temp = temp.next
            if temp == self.head and all(node.time == 0 for node in self._iter_nodes()):
                break

    def _iter_nodes(self):
        temp = self.head
        if not temp:
            return
        while True:
            yield temp
            temp = temp.next
            if temp == self.head:
                break

# Usage
scheduler = CPU_Scheduler()
scheduler.add_process("P1", 5)
scheduler.add_process("P2", 7)
scheduler.add_process("P3", 4)
scheduler.execute()
