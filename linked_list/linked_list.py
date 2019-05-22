'''
Linked List calculate define

1. certain element reference

2. list traversal

3. get lenth

4. insert element

5. delete element

6. merge list to list

'''
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None



class LinkedList:
    '''
    Node class을 통해 연결하고 구성된다.
    '''
    def __init__(self):
        self.nodeCount = 0
        self.head = None 
        self.tail = None
    
    def getAt(self, pos):
        if pos <= 0 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        data_list = []
        curr = self.head
        while curr is not None:
            data_list += [curr.data] # 모든 Node에 class에 data, next attribute을 가지고 있다.
            curr = curr.next
        return data_list
    

if __name__ == "__main__":
