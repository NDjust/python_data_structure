'''
popAt method 에러.
수정 예정.

popAfter method 및 더미코드 추가.

'''


class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
        return s

    def getLength(self):
        return self.nodeCount

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0  # dummy 추가로 수정.
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAfter(self, prev, newNode):
        newNode.next = prev.next

        if prev.next is None:
            self.tail = newNode

        prev.next = newNode
        self.nodeCount += 1

        return True

    def insertAt(self, pos, newNode):  # dummy node 아무것도 없는 임의의 노드
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail

        else:  # dummy로 맨앞일 경우 고려 x
            prev = self.getAt(pos - 1)

        return self.insertAfter(prev, newNode)

    def popAfter(self, prev):
        curr = prev.next
        if self.nodeCount == 1:
            self.head.next = None
            self.tail = None
        else:
            if curr.next is None:
                prev.next = None
                self.tail = prev
            else:
                prev.next = curr.next
        self.nodeCount -= 1
        return curr.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos - 1)

        return self.popAfter(prev)

    def traverse(self):
        result = []
        curr = self.head
        while curr.next:  # dummy 추가로 수정
            result.append(curr.data)
            curr = curr.next
        return result

    def concat(self, l):
        self.tail.next = l.head.next  # dummy 추가로 수정.
        if l.tail:
            self.tail = l.tail
        self.nodeCount += l.nodeCount


if __name__ == "__main__":
    # test cases
    a = Node(11)
    b = Node(15)
    c = Node(20)
    L = LinkedList()
    print(L)
    print(L.insertAt(1, a))
    print(L)
    print(L.insertAt(2, c))
    print(L.popAt(1))
    print(L.popAt(1))
    print(L.tail is None)
