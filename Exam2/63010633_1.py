class Stack:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(str(i))

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def bottom(self):
        if not self.isEmpty():
            return self.items[0]
        return -1

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return -1
    
    def __str__(self):
        return "Data in Stack is : " + ' '.join(self.items)

inp = int(input("Enter choice : "))
s1 = Stack()
if inp == 1:
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())
elif inp == 2:
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :",s1.isEmpty())
elif inp == 3:
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :",s1.size())
