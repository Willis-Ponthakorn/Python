def check(l,x,y):
    a = l[x] if x*2 > len(l)-2 else  l[x] + l[x*2] + l[x*2+1]  
    b = l[y] if y*2 > len(l)-2 else  l[y] + l[y*2] + l[y*2+1]
    if a>b:
        return str(x) + '>' +str(y) 
    elif a<b:
        return str(x) + '<' +str(y)
    else:
        return str(x) + '=' +str(y)

s = input('Enter Input : ').split('/')
l = [int(e) for e in s[0].split()]
ql = [e for e in s[1].split(',')]
print(sum(l))
for i in ql:
    i = i.split()
    print(check(l, int(i[0]),int(i[1])))
