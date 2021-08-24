x = [int(a) for a in input("Enter Your List : ").split()]
if len(x) < 3:
    print('Array Input Length Must More Than 2')
else:    
    temp = [0]*3
    ans = []
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            for k in range(j+1,len(x)):
                if x[i]+x[j]+x[k]==5:
                    temp[0] = x[i]
                    temp[1] = x[j]
                    temp[2] = x[k]
                    temp.sort()
                    ans.append(temp.copy())
    final = []
    for i in ans:
        if i not in final:
            final.append(i)
    print(final)
    
