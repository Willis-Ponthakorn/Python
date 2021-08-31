class Stack:
    def __init__(self):
        self.items = []
        self.items2 = []

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

    def manageStack(self, i):
        temp = i.split()
        if temp[0] == 'A':
            x = int(temp[1])
            self.items.append(x)
            return "Add = " + temp[1]
        elif temp[0] == 'P':
            if not self.isEmpty():
                x = self.top()
                self.items.pop()
                return "Pop = " + str(x)
            return -1
        elif temp[0] == 'D':
            if not self.isEmpty():
                str1 = ''
                a = 0
                while self.size() != a and self.size() != 0:
                    a = self.size()
                    for i in range(self.size()):
                        x = self.top()
                        self.items.pop()
                        if(x != int(temp[1])):
                            self.items2.append(x)
                        else:
                            self.items2 = self.items2[::-1]
                            for i in self.items2:
                                self.items.append(int(i))
                            self.items2 = []
                            str1 += "Delete = " + temp[1] + "\n"
                self.items2 = self.items2[::-1]
                
                for i in self.items2:
                    self.items.append(int(i))
                if temp[1] not in self.items:
                    self.items2 = []
                str1 = str1[:-1]
                return str1
            return -1
        elif temp[0] == 'LD':
            if not self.isEmpty():
                str1 = ""
                a = 0
                while self.size() != a and self.size() != 0:
                    a = self.size()
                    for i in range(self.size()):
                        x = self.top()
                        self.items.pop()
                        if(x >= int(temp[1])):
                            self.items2.append(x)
                        else:
                            self.items2 = self.items2[::-1]
                            for i in self.items2:
                                self.items.append(int(i))
                            self.items2 = []
                            str1 += "Delete = " + str(x) + " Because " + str(x) + " is less than " + temp[1] + "\n"
                self.items2 = self.items2[::-1]
                for i in self.items2:
                    self.items.append(int(i))
                if temp[1] not in self.items:
                    self.items2 = []
                str1 = str1[:-1]
                return str1
            return -1
        elif temp[0] == 'MD':
            if not self.isEmpty():
                str1 = ""
                a = 0
                while self.size() != a and self.size() != 0:
                    a = self.size()
                    for i in range(self.size()):
                        x = self.top()
                        self.items.pop()
                        if(x <= int(temp[1])):
                            self.items2.append(x)
                        else:
                            self.items2 = self.items2[::-1]
                            for i in self.items2:
                                self.items.append(int(i))
                            self.items2 = []
                            str1 += "Delete = " + str(x) + " Because " + str(x) + " is more than " + temp[1] + "\n"
                self.items2 = self.items2[::-1]
                for i in self.items2:
                    self.items.append(int(i))
                if temp[1] not in self.items:
                    self.items2 = []
                str1 = str1[:-1]
                return str1
            return -1

inp = input("Enter Input : ").split(',')
s = Stack()
for i in inp:
    str2 = s.manageStack(i)
    if str2 != '':
        print(str2)
print("Value in Stack =" , ([e for e in s.items]))