import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from DoublyLinkedList.DoublyLinkedList import DoublyLinkedList
from DoublyLinkedList.DoublyLinkedList import Node

class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def is_Empty(self):
        return self.data.getLength() == 0
    
    def enqueue(self, item):
        newNode = Node(item)
        return self.data.insertAt(self.data.nodeCount + 1, newNode)
    
    def dequeue(self):
        return self.data.popAt(1)

    def peek(self):
        return self.data.getAt(1).data

if __name__ == "__main__":
    q = LinkedListQueue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.data)
    print(q.is_Empty())
    print(q.size())
    print(q.peek())
    print(q.dequeue())
    print(q.dequeue())
    print(q.data)
    print(q.peek())
    print(q.is_Empty())
