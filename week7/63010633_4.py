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
        
    def delete(self, root, data):
        if root is None:
            return root
        if self.root:
            if self.root.data == data:
                if self.root.left is None and self.root.right is None:
                    self.root = None
                elif self.root.left is None:
                    self.root = self.root.right
                elif self.root.right is None:
                    self.root = self.root.left
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif(data > root.data):
            root.right = self.delete(root.right, data)
        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = root.right
            while temp.left is not None:
                temp = temp.left
            root.data = temp.data
 
            root.right = self.delete(root.right, temp.data)
 
        return root
    
    def find(self, root, key):
        if root is None or root.data == key:
            return root == None
        if root.data < key:
            return self.find(root.right,key)
        return self.find(root.left,key)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ').split(',')
for i in inp:
    temp = i.split()
    if temp[0] == 'i':
        print('insert',int(temp[1]))
        root = T.insert(int(temp[1]))
    if temp[0] == 'd':
        print('delete',int(temp[1]))
        if T.find(T.root, int(temp[1])):
            print('Error! Not Found DATA')
        root = T.delete(T.root, int(temp[1]))
        
    T.printTree(root)
