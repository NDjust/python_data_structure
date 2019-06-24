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

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
                curr = curr.next
        return s

    def getAt(self, pos):
        if pos <= 0 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def insertAt(self, pos, newNode):
        '''
        1. pos가 가리키는 위치에( 1 <= pos <= nodeCount + 1)
        2. newNode 를 삽입
        3. 성공/실패에 따라 true/false 를 리턴.

        주의사항
        1) 삽입하려는 위치가 리스트 맨앞일때
        -> prev 없음, head 조정 필요
        2) 삽입하려는 위치카 리스트 맨 끝일때
        -> tail 조정 필요.

        * 빈 리스트 일 경우는?

        insert function Complexity

        맨 앞에 경우 : O(1)

        중간에 경우 : O(n)

        맨 끝에 경우 : O(1)
        '''
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        if pos == 1:  # 조건문을 잘 처리 함으로써 빈 리스트의 경우도 처리할수록 설계.
            newNode.next = self.head
            self.head = newNode
        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)  # 왜 이 순서로 해야하는지 파악.
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode
        self.nodeCount += 1

        return True

    def popAt(self, pos):
        '''
        1. pos가 가리키는 위치의(1 <= pos <= nodeCount)
        2. node를 삭제
        3. node의 데이터를 리턴.

        주의사항.
        1) 삭제하려는 node가 맨앞의 것일때
        -> prev 없음, head 조정
        2) 리스트 맨 끝의 node를 삭제할 때 
        -> tail 조정 필요.

        유일한 노드를 삭제할때
        -> 위 조건 만으로 만족 하는가?

        삭제하려는 node 가 마지막 node 일 때,
        즉 pos == nodeCount 인 경우??
        -> insert처럼 한번에 처리 할 수 없다.(prev 를 찾을 방법이 없으므로)
        -> 앞에서부터 찾아와야 함.

        Complexity 
        맨 앞 : O(1)
        중간 : O(N)
        끝 : O(N)
        '''

        data = 0
        if pos <= 0 or pos > self.nodeCount:
            raise IndexError

        if pos == 1:
            data = self.head.data
            self.head = self.head.next
        else:
            prev = self.getAt(pos - 1)
            if pos == self.nodeCount:
                data = prev.next.data
                prev.next = None
                self.tail = prev
            else:
                data = prev.next.data
                prev.next = prev.next.next
        if self.nodeCount == 1:
            self.head = None
            self.tail = None

        self.nodeCount -= 1
        return data

    def concat(self, L):
        self.tail.next = L.head
        if L.tail:  # 빈 리스트 일 경우 조건 처리.
            self.tail = L.tail
        self.nodeCount += L.nodeCount

    def traverse(self):
        data_list = []
        curr = self.head
        while curr is not None:
            # 모든 Node에 class에 data, next attribute을 가지고 있다.
            data_list += [curr.data]
            curr = curr.next
        return data_list


if __name__ == "__main__":
    # insertAt test case
    a = Node(67)
    b = Node(34)
    c = Node(28)
    L = LinkedList()
    print(L)
    print(L.insertAt(1, a))
    print(L.insertAt(2, b))
    print(L.insertAt(1, c))
    # print(L.insertAt(2, c)) - > Node 중복시 에러.
    print(L.traverse())
    print(L.popAt(1))
    print(L.popAt(2))
    print(L.popAt(1))
