def min(num,li):
    if len(li) == 0:
        return num
    temp = li.pop()
    if num > temp:
        num = temp
    return min(num,li)

s = [int(e) for e in input('Enter Input : ').split()]
print('Min :',min(s[0],s))

