class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = Node(data)
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node(data)
                        break
                    curr = curr.right
            return self.root
    
    def findMin(self):
        if self.root is not None:
            curr = self.root
            while curr.left is not None:
                curr = curr.left
            return curr.data
        return None

    def findMax(self):
        if self.root is not None:
            curr = self.root
            while curr.right is not None:
                curr = curr.right
            return curr.data
        return None
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print("Min :",T.findMin())
print("Max :",T.findMax())