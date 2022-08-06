def natural_sum(x,l):
    if x>1:
        natural_sum(x-1,l)
    l.append(x)
    return l

print(' *** Natural sum ***')
s = int(input('Enter number : '))
    
print( ' + '.join([str(e) for e in natural_sum(s,[])]),'=',sum(natural_sum(s,[])))