print("*** Fun with Drawing ***")
x = int(input("Enter input : "))
r = 2*x-2
for y in range(-r,r+1):
    for x in range(-r,r+1):
        if abs(x)+abs(y)==abs(x)*2 and x%2==0:
            print("#",end="")
        elif abs(x)+abs(y)==abs(x)*2 and x%2==1:
            print(".",end="")
        elif abs(y)%2==1 and abs(x)%2==1:
            print(".",end="")
        elif abs(y)%2==0 and abs(x)%2==0:
            print("#",end="")
        elif abs(y)%2==1 and abs(x)%2==0 and abs(y)<abs(x):
            print("#",end="")
        elif abs(y)%2==0 and abs(x)%2==1 and abs(y)<abs(x):
            print(".",end="")
        elif abs(y)%2==1 and abs(x)%2==0 and abs(y)>abs(x):
            print(".",end="")
        elif abs(y)%2==0 and abs(x)%2==1 and abs(y)>abs(x):
            print("#",end="")
        else:
            print(" ",end="")
            
    print()