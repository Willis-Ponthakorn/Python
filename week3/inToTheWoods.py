class Stack:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        if not self.isEmpty():
            self.items.pop()
        return -1
    
    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        return -1

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

tree = input("Enter Input : ").split(',')
s = Stack()
for i in tree:
    temp = i.split()
    if(temp[0] == 'A'):
        temp2 = int(temp[1])
        if(s.isEmpty()):
            s.push(temp2)
        else:
            while temp2 >= s.top() and not s.isEmpty():
                s.pop()
            s.push(temp2)
    elif(temp[0] == 'B'):
        print(s.size())
