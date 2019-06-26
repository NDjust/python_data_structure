import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from DoublyLinkedList.DoublyLinkedList import Node, DoublyLinkedList

class PriorityQueue:

    def __init__(self):
        self.queue = DoublyLinkedList()

    def size(self):
        return self.queue.getLength()

    def is_Empty(self):
        return self.queue.nodeCount == 0

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head

        while curr.next != self.queue.tail and x < curr.next.data:
            curr = curr.next
        '''
         while x < curr.next.data and curr.next != self.queue.tail
         -> 만약 curr.next.data 가 None인 경우 TypeError: '<' not supported between instances of 'int' and 'NoneType'
         하지만 while curr.next.data != None and x < curr.next.data
         이런 순서로 할 경우에는 curr.next.data == None인 경우 뒤에 조건을 무시해 오류를 피해 갈 수 있다.
        '''
        self.queue.insertAfter(curr, newNode)
    
    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())
    
    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data
