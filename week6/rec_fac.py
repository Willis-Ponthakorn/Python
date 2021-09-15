def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fac(n-1) * n

inp = int(input('Enter Number : '))
print(inp,end='')
print('! =',fac(inp))