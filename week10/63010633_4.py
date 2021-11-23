def checkPrime(k):
    for i in range(2,k//2):
        if k%i == 0 :
            return False
    return True

def creatTable(l):
    sl = len(l)*2
    while checkPrime(sl) == False:
        sl+=1
    for i in range(sl-len(l)):
        l.append(None)
    return l

def rehash(l):
    for i in range(len(l)-1,-1,-1) :
        k = l[i]
        kc = k
        nCol = 0
        if l[i] is not None and l[k%len(l)] is None:
            k = (kc%len(l)+pow(nCol,2))%len(l)
        elif l[i] is not None and l[k%len(l)] is not None :
            if l[(k+1)%len(l)] is None and i!=k%len(l):
                print('collision number', nCol+1 ,'at',k%len(l))
                k = (kc%len(l)+pow(nCol+1,2))%len(l)          
        if l[i] is not None and l[k%len(l)] is None :
            l[i],l[k%len(l)] = l[k%len(l)],l[i]
    return l

def ins(l,nCol,mxCol,i):
    k = i%len(l)
    if l[k] is None:
        l[k] = i
        return l
    else:
        while nCol < mxCol and l[k] is not None:
            print('collision number', nCol+1 ,'at',k)
            nCol+=1
            k = (i+pow(nCol,2))%len(l)
            if nCol == mxCol :
                print('****** Max collision - Rehash !!! ******')
                l = creatTable(l)
                l = rehash(l)
                k = i%len(l)
                nCol = 0
        l[k] = i
        return l

def print_l(l):
    for j in range(len(l)):
        print('#'+str(j+1)+'	'+str(l[j]))
    print('----------------------------------------')

print(' ***** Rehashing *****')
s = input('Enter Input : ').split('/')
sTable, mxCol, thres = int(s[0].split()[0]),int(s[0].split()[1]),int(s[0].split()[2])
empl = 0
l = [None]*(sTable)

print('Initial Table :')
print_l(l)

for i in [int(e) for e in s[1].split()]:
    nCol = 0
    k = i%len(l)
    print('Add :',i)
    empl+=1
    if empl/len(l)*100 >= thres:
        print('****** Data over threshold - Rehash !!! ******')
        l = creatTable(l)
        l = rehash(l)
        ins(l,nCol,mxCol,i)
    else:
        ins(l,nCol,mxCol,i)
    print_l(l)
