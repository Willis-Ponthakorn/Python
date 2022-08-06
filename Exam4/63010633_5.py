comparisons = 0
def mergeSort(arr):
    global comparisons
    n = len(arr)
    if n > 1:
        mid = n // 2
        l1 = mergeSort(arr[:mid])
        l2 = mergeSort(arr[mid:])
        ss1, ss2 = len(l1), len(l2)
        i1, i2 = 0, 0
        res = []
        while i1 < ss1 and i2 < ss2:
            comparisons += 1
            if l1[i1] < l2[i2]:
                res.append(l1[i1])
                i1 += 1
            else:
                res.append(l2[i2])
                i2 += 1
        if i1 > i2:
            res += l2[i2:]
        elif i2 > i1:
            res += l1[i1:] 
        return res
    return arr

print(" *** Merge sort ***")
inp = [int(e) for e in input("Enter some numbers : ").split()]
print()
print('Sorted ->',' '.join(str(e) for e in mergeSort(inp)))
print('Data comparison = ',comparisons)