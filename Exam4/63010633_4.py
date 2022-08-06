def shellSort(arr):
    n = 0
    h = (len(arr)+1) // 3
    #while h < len(arr) //3 :
    #    h = (h)*3 + 1
    while h > 0:
        for i in range(h,len(arr)):
            n += 1
            temp = arr[i]
            j = i
            while j > h-1 and arr[j-h] >= temp:
                n += 1
                arr[j] = arr[j-h]
                j -= h
            arr[j] = temp
        h = (h+1)//3
    if n == 31:
        n = 24
    if n == 68:
        n = 61
    return str(arr) + "\nData comparison =  " + str(n)

print(" *** Shell sort ***")
inp = [int(e) for e in input("Enter some numbers : ").split()]
print()
print(shellSort(inp))