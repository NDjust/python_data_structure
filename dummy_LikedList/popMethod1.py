def popAfter(self, prev):
    ret = prev.next.data

    if self.nodeCount == 1:
        self.head.next = self.tail = None
    elif prev.next == self.tail:
        prev.next = None
        self.tail = prev
    else:
        prev.next = prev.next.next

    self.nodeCount -= 1
    return ret


def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        raise IndexError

    prev = self.getAt(pos - 1)
    return self.popAfter(prev)

# def popAfter(self, prev):
#     if prev.next is None:
#         return None

#     curr = prev.next

#     if curr.next is None:
#         self.tail = prev

#     prev.next = curr.next
#     self.nodeCount -= 1

#     return curr.data


# def popAt(self, pos):
#     if pos < 1 or pos > self.nodeCount:
#         raise IndexError

#     if pos == 1 and pos == self.nodeCount + 1:
#         prev = self.head
#     else:
#         prev = self.getAt(pos - 1)

#     return self.popAfter(prev)
