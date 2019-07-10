class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
    
    def size(self):
        l_s = self.left.size() if self.left else 0
        r_s = self.right.size() if self.right else 0
        return l_s + r_s + 1

    def depth(self):
        l_d = self.left.depth() if self.left else 0
        r_d = self.right.depth() if self.right else 0
        return max(l_d, r_d) + 1

    def inorder(self) -> list:
        '''
        ordering 
        1) left subtree
        2) self
        3) right subtree
        '''
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def preorder(self) -> list:
        '''
        ordering
        1) self
        2) left subtree
        3) right subtree
        '''
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal
    
    def postorder(self) -> list:
        '''
        ordering
        1) left subtree
        2) right subtree
        3) self
        '''
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0

    def inorder(self)->list:
        if self.root:
            return self.root.inorder()
        else:
            return []

    def preorder(self)->list:
        if self.root:
            return self.root.preorder()
        else:
            return []

    def postorder(self)->list:
        if self.root:
            return self.root.postorder()
        else:
            return []

   

