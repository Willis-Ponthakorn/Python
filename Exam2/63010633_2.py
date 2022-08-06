class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def enQueue(self,i):
        self.items.append(str(i))

    def deQueue(self):
        if not self.isEmpty():
            self.items.pop(0)
    
    def __str__(self):
        if not self.isEmpty():
            return "Queue data : " + ' '.join(self.items)
        return "Empty Queue"

inp = int(input("Enter choice : "))
q1 = Queue()
if inp == 1:
    q1.enQueue(10)
    q1.enQueue(20)
    q1.enQueue(30)
    print(q1)
    q1.deQueue()
    q1.enQueue(40)
    print("Size of Queue :",len(q1))
    print(q1)

elif inp == 2:
    q1 = Queue()
    q1.enQueue(100)
    q1.enQueue(200)
    q1.enQueue(300)
    q1.deQueue()
    print(q1)
    print("Queue is Empty :",q1.isEmpty())
elif inp == 3:
    q1 = Queue()
    q1.enQueue(11)
    q1.enQueue(22)
    q1.enQueue(33)
    q1.deQueue()
    q1.deQueue()
    q1.deQueue()
    print(q1)
    print("Size of Queue :",len(q1))
    print("Queue is Empty :",q1.isEmpty())