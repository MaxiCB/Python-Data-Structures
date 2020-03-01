import sys

sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = []

    # Add item to back of queue - tail
    def enqueue(self, value):
        self.storage.append(value)

    # Remove the item form the front of the queue
    def dequeue(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop(0)

    def len(self):
        return len(self.storage)
