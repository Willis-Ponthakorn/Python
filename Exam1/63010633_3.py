inp = [int(x) for x in input("Enter number end with (-1) : ").split()]
li = []
chli = [0] * (max(inp)+1)
check = False
for i in inp:
    if i == -1:
        check = True
        break
    li.append(i)
    chli[i]+=1
if not check:
    print("Invalid INPUT !!!")
else:
    get = False
    for i in li:
        if chli[i] > len(li)/2:
            print(i)
            get = True
            break
    if not get:
        print("Not found")