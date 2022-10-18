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
        if not self.is_full():
            if self.last > self.N:
                self.last = 0
            self.storage[self.last] = item
            self.last = self.N+1
        else:
            raise RuntimeError("Queue full")
        self.N += 1

    def dequeue(self):
        """If not empty, dequeue head in O(1) performance."""
        if not self.is_empty():
            head = self.storage[self.first]
            self.last = self.first
            self.first += 1
            if self.first == self.N:
                self.first = 0
            self.N -= 1
            return head
        else:
            raise RuntimeError("Queue empty")
        


if __name__ == "__main__":
    size = 4
    queue = Queue(size)
    queue.enqueue(20)
    queue.enqueue(2)
    queue.enqueue(23)
    queue.enqueue(1)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(15)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(18)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(17)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(9)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(4)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(3)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(15)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(18)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(17)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(9)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(4)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(3)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(4)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(3)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(15)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(18)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(17)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(9)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(4)
    print(queue.storage)
    print(queue.dequeue())
    queue.enqueue(3)
    print(queue.storage)




