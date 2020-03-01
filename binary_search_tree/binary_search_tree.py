import sys
sys.path.append('../queue_and_stack')
from queue_and_stack.dll_queue import Queue
from queue_and_stack.dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If the value is less than the previous value it goes left
        # If the value is more than the previous value it goes right
        if value <= self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if self.right is None and self.left is None:
            return False
        if self.left and target < self.value:
            return self.left.contains(target)
        if self.right and target > self.value:
            return self.right.contains(target)
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        level = Queue()
        level.enqueue(node)
        while level.len() > 0:
            next_level = Queue()
            while level.len() > 0:
                curr_node = level.dequeue()
                if curr_node.left:
                    next_level.enqueue(curr_node.left)
                if curr_node.right:
                    next_level.enqueue(curr_node.right)
                print(curr_node.value)
            level = next_level

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        branches = Stack()
        branches.push(node)
        while branches.len() > 0:
            cur_node = branches.pop()
            print(cur_node.value)
            if cur_node.left:
                branches.push(cur_node.left)
            if cur_node.right:
                branches.push(cur_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)
