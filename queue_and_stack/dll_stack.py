import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list.doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop(len(self.storage) - 1)

    def len(self):
        return len(self.storage)
