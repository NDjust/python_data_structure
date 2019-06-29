class Node:

    def __init__(self,key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal
    
    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent
            
    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self
    
    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError('Duplicate Key')

    def countChildern(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None
    
    def min(self):
        if self.root:
            return self.root.min()
        else:
            return None
    
    def max(self):
        if self.root:
            return self.root.max()
        else:
            return None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)
    
    def remove(self, key):
        node, parent = self.lookup(key)
        Countchild = node.countChildern()
        if node:
            if Countchild == 0:
                if parent:
                    if parent.key > key:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.root = None

            elif Countchild == 1:
                if node.left:
                    node_child = node.left
                else:
                    node_child = node.right
                
                if parent:
                    if parent.key > key:
                        parent.left = node_child
                    else:
                        parent.right = node_child
                else:
                    self.root = node_child
            else: # if childe node count is 2, how to remove node.
                pass    
            

        else:
            return False
            
