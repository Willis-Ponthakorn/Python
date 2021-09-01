inp = input('Enter Input : ').split()
combo = 0

while True:
    pop = False
    counter = 0
    color = ""
    sIndex = -1
    for i in range(len(inp)-1):
        if sIndex < 0:
            color = inp[i]
            sIndex = i
            counter = 1
        if color != inp[i]:
            color = inp[i]
            sIndex = i
            counter = 1
        else:
            counter += 1
        if counter == 3:
            pop = True
            combo += 1
            for j in range(3):
                inp.pop(sIndex)
            break
    if not pop:
        break

print(len(inp))
if len(inp) == 0:
    print("Empty")
else:
    for i in inp[::-1]:
        print(i,end="")
    print()
if combo > 1:
    print("Combo :",combo,"! ! !")
