def insertionSort(li, li_s, n=0):
    if len(li) == 0:
        print('sorted')
    if len(li_s) == 0:
        li_s.append(li.pop(0))
        li_s = insertionSort(li, li_s, n)
    if n < len(li_s) and len(li) > 0:
        if li[0] > li_s[n]:
            li_s = insertionSort(li, li_s, n+1)
        else:
            li_s.insert(n,li.pop(0))
            print('insert',li_s[n],'at index',n,':',li_s,end=' ')
            if len(li) > 0:
                print(li)
            else:
                print()
            li_s = insertionSort(li, li_s, 0)
    elif len(li) > 0:
        li_s.insert(n,li.pop(0))
        print('insert',li_s[n],'at index',n,':',li_s,end=' ')
        if len(li) > 0:
            print(li)
        else:
            print()
        li_s = insertionSort(li, li_s, 0)
    return li_s

inp = [int(i) for i in input('Enter Input : ').split()]
li_s = []
print(insertionSort(inp, li_s))
