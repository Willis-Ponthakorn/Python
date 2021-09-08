class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self):
        self.head = None

    def pushHead(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def pushTail(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        now = self.head
        while now.next != None:
            now = now.next
        now.next = newNode
        newNode.next = None
        newNode.prev = now

    def insert(self,index,data):
        ide = 0
        now = self.head
        newNode = Node(data)
        while ide < index:
            ide += 1
            now = now.next
        if self.head == None and ide == 0:
            self.pushTail(data)
        elif ide == 0:
            self.pushHead(data)
        elif ide == self.len():
            self.pushTail(data)
        elif now.prev != None:
            now.prev.next = newNode
            newNode.prev = now.prev
            now.prev = newNode
            newNode.next = now
    
    def removeLeft(self,index):
        if index == 0:
            return
        now = self.head
        ide = 0
        while ide < index-1:
            ide += 1
            now = now.next
        if now != None:
            now.prev.next = now.next
            now.next.prev = now.prev

    def removeRight(self,index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            now = self.head
            ide = 0
            while ide < index:
                ide += 1
                now = now.next
            if now is not None:
                if now.next is not None:
                    now.next.prev = now.prev
                if now.prev is not None:
                    now.prev.next = now.next
                else:
                    now.next.prev = None

    def __str__(self):
        now = self.head
        s = ''
        while now != None:
            s += str(now.data)
            if now.next != None:
                s += ' '
            now = now.next
        return s

    def len(self):
        now = self.head
        len = 0
        while now != None:
            len += 1
            now = now.next
        return len

inp = input('Enter Input : ').split(',')
ll = LinkedList()
index = 0
for i in inp:
    temp = i.split()
    if temp[0] == 'I':
        ll.insert(index, temp[1])
        index += 1
    elif temp[0] == 'L':
        if index > 0:
            index -= 1
    elif temp[0] == 'R':
        if index < ll.len():
            index += 1
    elif temp[0] == 'B':
        ll.removeLeft(index)
        if index > 0:
            index -= 1
    elif temp[0] == 'D':
        ll.removeRight(index)
ll.insert(index, '|')
print(ll)