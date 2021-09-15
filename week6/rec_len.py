a = 0
def length(txt):
    global a
    if txt == '':
        print()
        return 0
    if a == 0:
        print(txt[0],end='*')
        a += 1
    else:
        print(txt[0],end='~')
        a -= 1
    
    return 1 + length(txt[1:])

inp = input('Enter Input : ')
print(length(inp))