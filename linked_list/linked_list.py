'''
popAt method 에러.

수정 예정.
'''


class Node:

    def __init__(self, data):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.nodecount = 0

    def getAt(self, pos):
        if pos <= 0 or pos > self.nodecount:
            return None

        i = 1
        cur = self.head
        while i < pos:
            cur = cur.next
            i += 1
        return cur

    def insertAt(self, pos, newnode):
        if pos < 0 or pos > self.nodecount + 1:
            return False

        if pos == 1:
            newnode.next = self.head
            self.head = newnode
        else:
            if pos == self.nodecount + 1:
                prev = self.tail
            else:
                prev == self.getAt(pos - 1)
            newnode.next = prev.next
            prev.next = newnode

        if pos == self.nodecount + 1:
            self.tail = newnode

        return True

    def getLength(self):
        return self.nodecount

    def traverse(self):
        data = []
        cur = self.head

        while cur:
            data += [cur.data]
            cur = cur.next

        return data

    def popAt(self, pos):
        data = 0
        if pos <= 0 or pos > self.nodecount:
            raise IndexError

        if self.nodecount == 1:
            data = self.head.data
            self.head = None
            self.tail = None

        else:
            if pos == 1:
                data = self.head.data
                self.head = self.head.next

            else:
                prev = self.getAt(pos - 1)
                if pos == self.nodecount:
                    data = prev.next.data
                    prev.next = None
                    self.tail = prev
                else:
                    data = prev.next.data
                    prev.next = prev.next.next

        self.nodecount -= 1
        return data
