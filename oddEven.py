def odd_even(arr,s):
    if isinstance(arr,list):
        s_ans = []
        for x in range(0,len(arr)):
            if(s == 'Even' and x%2==1):
                s_ans.append(arr[x])
            elif(s == 'Odd' and x%2==0):
                s_ans.append(arr[x])
    elif isinstance(arr,str):
        s_ans = ''
        for x in range(0,len(arr)):
            if(s == 'Even' and x%2==1):
                s_ans += arr[x]
            elif(s == 'Odd' and x%2==0):
                s_ans += arr[x]
    
    return s_ans
print('*** Odd Even ***')
t,s,oe = input("Enter Input : ").split(",")
if t == 'S':
    s = str(s)
elif t == 'L':
    s = s.split(' ')
print(odd_even(s,oe))
