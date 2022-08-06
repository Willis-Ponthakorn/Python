def insertionSort(arr):
    newarr = []
    n = 0
    while len(arr) > 0:
        if len(newarr) == 0:
            newarr.append(arr.pop(0))
        else:
            i = 0
            if newarr[-1] < arr[0]:
                newarr.append(arr.pop(0))
                n += 1
            elif len(newarr) == 1:
                newarr.insert(0, arr.pop(0))
                n += 1
            else:
                while len(newarr) > i and newarr[-1-i] > arr[0] :
                    i += 1
                    n += 1
                newarr.insert(-1-i, arr.pop(0))
    return str(newarr) + "\nData comparison =  " + str(n)

print(" *** Insertion sort ***")
inp = [int(e) for e in input("Enter some numbers : ").split()]
print()
print(insertionSort(inp))