class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return -1

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

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
    
    def _pre(self):
        print('Prefix :',''.join([str(e) for e in self.preorder(self.root,[])])  )

    def _in(self):
        print('Infix :',''.join([str(e) for e in self.inorder(self.root,[])])  )
    
    def preorder(self,node,l):
        if node:
            l.append(node.data)
            self.preorder(node.left,l)
            self.preorder(node.right,l)
        return l

    def inorder(self,node,l):
        if node:
            if node.left is not None or node.right is not None:
                l.append('(')
            self.inorder(node.left,l)
            l.append(node.data)
            self.inorder(node.right,l)
            if node.left is not None or node.right is not None:
                l.append(')')
        return l
        
    def postorder(self,node,l):
        if node:
            self.postorder(node.left,l)
            self.postorder(node.right,l)
            l.append(node.data)
        return l

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

inp = input("Enter Postfix : ")
T = BST()
s = Stack()
for i in inp:
    if i in '+-*/':
        temp1 = s.pop()
        temp2 = s.pop()
        s.push(Node(i, temp2, temp1))
    else:
        s.push(Node(i))
print('Tree :')
T.root = s.pop()
T.printTree(T.root)
print('--------------------------------------------------')
T._in()
T._pre()