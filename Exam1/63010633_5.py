class MyInt:
    def __init__(self,x):
        self.num = int(x)
    
    def isPrime(self):
        temp = 0
        if self.num < 2:
            return False
        for i in range(2,int(self.num/2)):
            if self.num%i == 0:
                temp+=1
        return temp==0
    
    def showPrime(self):
        templi = [0]*(self.num+1)
        retli = []
        if self.num < 2:
            return "!!!A prime number is a natural number greater than 1"
        for i in range(2,self.num+1):
            if templi[i] == 0:
                mul = 2
                temp = i
                while temp < self.num:
                    temp = i*mul
                    mul+=1
                    if temp < len(templi):
                        templi[temp] = 1
        for i in range(2,len(templi)):
            if templi[i] == 0:
                retli.append(str(i))
        return " ".join(retli)

    def __sub__(self,other):
        return self.num - int(other.num/2)

print(" *** class MyInt ***")
inp = [int(x) for x in input("Enter 2 number : ").split()]
a = MyInt(inp[0])
b = MyInt(inp[1])
print(a.num,"isPrime :",a.isPrime())
print(b.num,"isPrime :",b.isPrime())
print("Prime number between 2 and",a.num,":",a.showPrime())
print("Prime number between 2 and",b.num,":",b.showPrime())
print(a.num,"-",b.num,'=',a-b)