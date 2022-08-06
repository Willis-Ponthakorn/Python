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

        if curr.data >= data:
            n.next = curr
            self.head = n
            return

        while curr.next is not None:
            if curr.data <= data and curr.next.data >= data:
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
        s = 'Linked data : '
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

def findMean(i):
    temp = i.head
    sum = temp.data
    while temp.next != None:
        sum += temp.next.data
        temp = temp.next
    mean = sum/len(i)
    print("Mean = %.2f" % mean)

def findMedian(x):
    temp = x.head
    for i in range(len(x)//2 - 1):
        temp = temp.next
    if len(x)%2 == 0:
        med = (temp.data+temp.next.data)/2
    else:
        med = temp.next.data
    
    print("Median = %.2f" % med)

inputlist = [int(e) for e in input('Enter numbers : ').split()]
l = LinkedList()
for i in inputlist:
    l.pushTail(i)
print("Output :")
print(l)
print('Amount of data =',len(l))
findMean(l)
findMedian(l)