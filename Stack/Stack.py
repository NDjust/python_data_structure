import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# 1단계 위 부모폴더의 절대경로를 참조 path에 추가.
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname((os.path.dirname(__file__)))))) - 2단계 위 부모 폴더의 절대경로를 참조 path에 추가.


from DoublyLinkedList.DoublyLinkedList import Node
from DoublyLinkedList.DoublyLinkedList import DoublyLinkedList

class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


class LinkedListStack:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        node = Node(item)
        self.data.insertAt(self.size() + 1, node)

    def pop(self):
        return self.data.popAt(self.size())

    def peek(self):
        return self.data.getAt(self.size()).data
