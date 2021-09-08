class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def pushHead(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pushTail(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        now = self.head
        while now.next:
            now = now.next
        now.next = newNode
        newNode.next = None

    def popHead(self):
        self.head = self.head.next

    def popTail(self):
        newNode = self
        if self.head is None:
            self = newNode
            return
        now = self.head
        while now.next.next:
            now = now.next
        now.next = None

    def len(self):
        now = self.head
        len = 0
        while now != None:
            len += 1
            now = now.next
        return len

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        now = self.head
        s = ''
        while now != None:
            s += str(now.data)
            if now.next != None:
                s += ' <- '
            now = now.next
        return s
    
    def isIn(self,data):
        now = self.head
        while now != None:
            if now == data:
                return True
            now = now.next
        return False

inp = input(' *** Locomotive ***\nEnter Input : ').split()
bef = LinkedList()
aft = LinkedList()
for i in inp:
    bef.pushTail(int(i))
print('Before :',bef)
check = False
for i in inp:
    if i == '0' or check:
        aft.pushTail(int(i))
        check = True
for i in inp:
    if i == '0':
        break
    aft.pushTail(int(i))
print('After :',aft)