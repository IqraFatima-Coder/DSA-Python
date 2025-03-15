class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.max_size = size
        self.front = self.rear = -1

    def enqueue(self, song):
        """Add a song to the queue."""
        if (self.rear + 1) % self.max_size == self.front:
            print("Playlist is full!")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = song

    def dequeue(self):
        """Remove a song from the queue."""
        if self.front == -1:
            print("No songs in playlist!")
            return None
        song = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return song

    def play_all(self):
        """Play all songs in circular order."""
        while self.front != -1:
            print("Now playing:", self.dequeue())

# Example Usage
playlist = CircularQueue(5)
playlist.enqueue("Song 1")
playlist.enqueue("Song 2")
playlist.enqueue("Song 3")
playlist.play_all()
