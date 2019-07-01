class MaxHeap:

    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        last_index = len(self.data) - 1
        while last_index > 1:
            parent = last_index // 2
            if self.data[parent] < self.data[last_index]:
                self.data[parent], self.data[last_index] = self.data[last_index], self.data[parent]
                last_index = last_index // 2
            else:
                break

    def remove(self):
        if len(self.data) > 1:
            self.data[-1], self.data[1] = self.data[1], self.data[-1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data

    def maxHeapify(self, i):
        left = i * 2
        right = i * 1 + 1
        smallest = i
        
        if left < len(self.data) - 1 and self.data[left] > self.data[right]:
            smallest = left
        elif right < len(self.data) - 1 and self.data[right] > self.data[left]:
            smallest = right
        
        if i != smallest:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.maxHeapify(smallest)
