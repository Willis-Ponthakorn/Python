class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, ntable, maxColl):
        self.table = [None]*ntable
        self.maxColl = maxColl
    
    def hashing(self, data, n=0, coll=0):
        if None not in self.table:
            return -1
        index = 0
        for i in data.key:
            index += ord(i)
        index += pow(n,2)
        index %= len(self.table)
        if self.table[index] is None:
            self.table[index] = data
        elif coll < self.maxColl:
            print('collision number',coll+1,'at',index)
            self.hashing(data,n+1,coll+1)
        else:
            print('Max of collisionChain')
        return 0

    def __str__(self):
        s = ''
        for i in range(len(self.table)):
            s += '#'+str(i+1)+'      '+str(self.table[i])
            if i != len(self.table)-1:
                s+='\n'
        return s

print(" ***** Fun with hashing *****")
inp = input('Enter Input : ').split('/')
h = hash(int(inp[0].split()[0]),int(inp[0].split()[1]))
for i in inp[1].split(','):
    dat = Data(i.split()[0],i.split()[1])
    temp = h.hashing(dat)
    if temp == -1:
        print('This table is full !!!!!!')
        break
    print(h)
    print('---------------------------')