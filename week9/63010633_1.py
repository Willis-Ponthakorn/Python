def swap(li, i ,j):
    temp = li[i]
    li[i] = li[j]
    li[j] = temp
    return li

def bubbleSort(li, n):
    if n - 1 >= 0:
        if li[n] < li[n-1]:
            li = swap(li,n,n-1)
            li = bubbleSort(li, len(li)-1)
        li = bubbleSort(li, n - 1)
    return li

inp = [int(i) for i in input('Enter Input : ').split()]
print(bubbleSort(inp,len(inp)-1))
