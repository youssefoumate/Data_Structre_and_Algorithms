"""Heap Module
"""
class Queue:
    """Circular Queue
    """
    def __init__(self, size):
        """initializa queue

        Args:
            size (int): _description_
        """
        self.size = size
        self.storage = [None] * size
        self.first = 0
        self.last = 0
        self.N = 0
    def is_empty(self):
        return self.N == 0
    def is_full(self):
        return self.N == self.size
    def enqueue(self, item):
        """If not full, enqueue item in O(1) performance."""
        if self.N == 0:
            self.first = self.N
            self.last = self.N
            self.storage[self.N] = item
        elif self.N < 16:
            self.storage[self.N] = item
        else:
            raise RuntimeError("queue full")
        self.N += 1

    def dequeue(self):
        """If not empty, dequeue head in O(1) performance."""
        head = self.storage[self.first] 
        if not self.first > self.size:
            self.first += 1
        


if __name__ == "__main__":
    size = 4
    queue = Queue(size)
    queue.enqueue(20)
    queue.enqueue(2)
    queue.enqueue(23)
    queue.enqueue(1)
    print(queue.storage)



