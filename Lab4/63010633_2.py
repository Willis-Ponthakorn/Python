class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enQueue(self,i):
        self.items.append(i)
        return "Add " + i + " index is " + str(self.size()-1)

    def deQueue(self):
        if not self.isEmpty():
            temp = self.items[0]
            self.items.pop(0)
            return "Pop " + temp + " size in queue is " + str(self.size())
        return -1
    
    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        return -1

inp = input("Enter people : ")
q = Queue()
c1 = Queue()
c2 = Queue()
timer = 0
c1_count = 0
c2_count = 0
c1_start = False
c2_start = False
for i in inp:
    q.enQueue(i)
while q.size() != 0:
    if c1_start:
        c1_count+=1
        if c1_count == 3:
            c1.deQueue()
            c1_count = 0
    if c2_start:
        c2_count+=1
        if c2_count == 2:
            c2.deQueue()
            c2_count = 0
    if c1.size() < 5:
        c1.enQueue(q.peek())
        c1_start = True
        q.deQueue()
    elif c1.size() == 5 and c2.size() < 5:
        c2.enQueue(q.peek())
        c2_start = True
        q.deQueue()
    timer +=1
    print(str(timer),([x for x in q.items]),([x for x in c1.items]),([x for x in c2.items]))

