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

inp = input('Enter Input : ').split()
bef = []
li = []
num = [LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList()]
digit = 0
size = len(inp)
keep = False
while num[0].len() != size:
    digit += 1
    for i in inp:
        if not keep:
            bef.append(i)
        temp = int(i)
        if temp < 0:
            temp *= -1
            temp = int(((temp - (int(i)*-1) % (pow(10,digit-1)))/pow(10,digit-1))%10)
        else:
            temp = int(((temp - int(i) % (pow(10,digit-1)))/pow(10,digit-1))%10)
        num[temp].pushTail(int(i))
        if temp == 0:
            li.append(i)
    keep = True
    for i in li:
        inp.remove(i)
    li = []
    print('------------------------------------------------------------')
    print('Round :',str(digit))
    print('0 :',num[0])
    for i in range(1,len(num)):
        print(i,':',num[i])
        num[i] = LinkedList()

print('------------------------------------------------------------')
print(str(digit-1),'Time(s)')
print('Before Radix Sort :',' -> '.join(bef))
print('After  Radix Sort :',' -> '.join(str(num[0]).split()))