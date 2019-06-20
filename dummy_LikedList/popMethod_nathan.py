'''
1. 맨앞의 리스트를 pop 할경우
2. 리스트가 한개일 경우
3. 맨뒤의 리스트를 pop할 경우

* dummy node 고려해서 코드 짜기.
'''


def popAfter(self, prev):
    if prev.next is None:
        return None
    curr = prev.next

    if self.nodeCount != 1 and curr.next is None:
        self.tail = prev

    prev.next = curr.next
    self.nodeCount -= 1

    return curr.data


def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        raise IndexError
    if self.nodeCount == 1:
        prev = self.tail
    else:
        prev = self.getAt(pos - 1)

    return self.popAfter(prev)
