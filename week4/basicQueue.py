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

inp = input("Enter Input : ").split(",")
q = Queue()
for i in inp:
    hello = i.split()
    if hello[0] == 'E':
        print(q.enQueue(hello[1]))
    elif hello[0] == 'D':
        print(q.deQueue())
if q.size() == 0:
    print("Empty")
else:
    print("Number in Queue is : " , ([x for x in q.items]))