def bubbleSort(li):
    for i in range(len(li)-1,0,-1):
        for j in range(i):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    return li

inp = input('Enter Input : ').split()
d = dict()
li = []
for i in inp:
    for j in i:
        if j.isalpha():
            d.update({j:i})
            li.append(j)
li = bubbleSort(li)
for i in li:
    print(d[i],end=' ')
