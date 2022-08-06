class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def pushTail(self,data):
        curr = self.head
        n = Node(data)
        if curr is None:
            self.head = n
            return

        if curr.data > data:
            n.next = curr
            self.head = n
            return

        while curr.next is not None:
            if curr.data < data and curr.next.data > data:
                break
            curr = curr.next
        n.next = curr.next
        curr.next = n

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

    def __len__(self):
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
                s += ' '
            now = now.next
        return s
    
    def isIn(self,data):
        now = self.head
        while now != None:
            if now == data:
                return True
            now = now.next
        return False

    def contentEquivalence(self,other):
        check = 1
        temp1 = self.head
        temp2 = other.head
        while temp1.next != None:
            if temp1.data != temp2.data or len(self) != len(other):
                check = 0
                break
            temp1 = temp1.next
            temp2 = temp2.next
        if temp1.data != temp2.data:
                check = 0
        if check == 1:
            return "True"
        return "False"

inp = input("List1,List2 : ").split(',')
li1 = inp[0].split()
li2 = inp[1].split()
ll1 = LinkedList()
ll2 = LinkedList()
for i in li1:
    ll1.pushTail(i)
for i in li2:
    ll2.pushTail(i)
print("List1 content Equivalence List2 :",ll1.contentEquivalence(ll2))