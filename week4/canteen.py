class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return -1
    
    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        return -1

    def inSec(self, sec):
        for i in self.items:
            if sec == i[0]:
                return True
        return False

    def cutIn(self,i):
        if self.isEmpty() or not self.inSec(i[0]):
            self.enQueue(i)
        else:
            for x in range(self.size()-1, -1, -1):
                if self.items[x][0] == i[0]:
                    self.items.insert(x+1, i)
                    return
            self.enQueue(i)

inp = input("Enter Input : ").split('/')
q = Queue()
temp = inp[0].split(',')
emp = dict()
for i in temp:
    sec, id = i.split()
    emp[id] = sec
temp = inp[1].split(',')
for i in temp:
    hello = i.split()
    if hello[0] == 'D':
        if q.isEmpty():
            print("Empty")
        else:
            print(q.deQueue()[1])
    elif hello[0] == 'E':
        que = i.split()
        ide = que[1]
        q.cutIn((emp[ide], ide))
