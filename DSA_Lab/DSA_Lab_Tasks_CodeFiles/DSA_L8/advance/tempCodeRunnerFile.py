class PacketQueue:
    def __init__(self):
        self.queue = []

    def send_packet(self, packet):
        """Add a packet to the queue."""
        self.queue.insert(0, packet)

    def process_packet(self):
        """Process packets in FIFO order."""
        if self.queue:
            return f"Processing packet: {self.queue.pop()}"
        return "No packets to process."

# Example Usage
network = PacketQueue()
network.send_packet("Packet 1")
network.send_packet("Packet 2")
print(network.process_packet())  # Processing packet: Packet 1
print(network.process_packet())  # Processing packet: Packet 2
