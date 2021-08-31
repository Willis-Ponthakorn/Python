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

print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)
sta1 = Stack()
sta2 = Stack()
car = s.split(',')
for i in car:
    if(int(i) != 0):
        sta1.push(int(i))
if o == 'arrive':
    if sta1.size() == m:
        print("car",n,"cannot arrive : Soi Full")
    elif n in sta1.items:
        print("car",n,"already in soi")
    else:
        sta1.push(n)
        print("car",n,"arrive! : Add Car",n)
elif o == 'depart':
    if int(s[0]) == 0:
        print("car",n,"cannot depart : Soi Empty")
    elif n not in sta1.items:
        print("car",n,"cannot depart : Dont Have Car",n)
    else:
        while(sta1.top() != n):
            sta2.push(sta1.top())
            sta1.pop()
        sta1.pop()
        while(sta2.size() != 0):
            sta1.push(sta2.top())
            sta2.pop()
        print("car",n,"depart ! : Car",n,"was remove")
print([e for e in sta1.items])  