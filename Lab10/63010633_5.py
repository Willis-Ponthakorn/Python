inp = input('Enter Input : ').split('/')
l = [int(e) for e in inp[0].split()]
box = int(inp[1])
lim = max(l)
minW = []
while len(minW) != box:
    temp,minW = [],[]
    for i in l:
        if sum(temp) + i <= lim:
            temp.append(i)
        else:
            minW.append(sum(temp))
            temp = [i]
    minW.append(sum(temp))
    lim += 1
print('Minimum weigth for',inp[1],'box(es) =',max(minW))