class CircularQueue:

    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1
        

    def size(self):
        return self.count

    def is_Empty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue full')
        self.rear = 0 if self.rear == self.maxCount - 1 else self.rear + 1
        # self.rear = (self.rear + 1) % (self.maxCount)
        self.data[self.rear] = x
        self.count += 1
    
    def dequeue(self):
        if self.is_Empty():
            raise IndexError('Queue empty')
        self.front = 0 if self.front == self.maxCount - 1 else self.front + 1
        # self.front = (self.front + 1) % (self.maxCount)
        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):
        if self.is_Empty():
            raise IndexError('Queue empty')
        return self.data[0 if self.front == self.maxCount - 1 else self.front + 1]
        # return self.data[(self.front + 1) % (self.maxCount)]