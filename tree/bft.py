class ArrayQueue:
    
    def __init__(self, item):
        self.data = []

    def size(self):
        return len(self.data())

    def isEmpty(self):
        return self.size() == 0
    
    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:
    
    def __init__(self, r):
        self.root = r

    def bft(self):
        traversal = []
        q = ArrayQueue()
        
        if self.root:
            q.enqueue(self.root)
        
        while not q.isEmpty(): # 부모 노드의 순서에 따라 다음 노드들의 순서가 결정됨으로 한 노드 방문시 그 다음 노드들 순서를 기록.
            node = q.dequeue()
            traversal.append(node.data)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

        return traversal