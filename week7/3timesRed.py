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

    def print3Tree(self, node, k, level = 0):
        if node != None:
            self.print3Tree(node.right, k, level + 1)
            if node.data <= k:    
                print('     ' * level, node)
            else:
                print('     ' * level, node.data*3)
            self.print3Tree(node.left, k, level + 1)

T = BST()
inp = input('Enter Input : ').split('/')
data = [int(i) for i in inp[0].split()]
k = int(inp[1])
for i in data:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
T.print3Tree(root,k)
