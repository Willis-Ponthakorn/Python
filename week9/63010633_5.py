class dic:
    def __init__(self,s,w,l,d,sc,con):
        self.s = s
        self.tp = 3*w+0*l+1*d
        self.gf = sc-con
    def __str__(self):
        return "['"+self.s+"', {'points': "+str(self.tp)+"}, {'gd': "+str(self.gf) + "}]"

def bubbleSort(li):
    for i in range(len(li)-1,0,-1):
        for j in range(i):
            if li[j].tp < li[j+1].tp:
                li[j],li[j+1] = li[j+1],li[j]
            elif l[j].tp == li[j+1].tp:
                if li[j].gf < li[j+1].gf:
                    li[j],li[j+1] = li[j+1],li[j]
    return li

s = [str(e).split(',') for e in input('Enter Input : ').split('/')]
l = [ dic( e[0],int(e[1]),int(e[2]),int(e[3]),int(e[4]),int(e[5])) for e in s]
print('== results ==\n'+'\n'.join([str(e) for e in bubbleSort(l)]))
