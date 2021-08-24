n = int(input("Enter Input : "))
for y in range(0,2*n+4):
    for x in range(0,2*n+4):
        if x+y < n+1:
            print(".",end="")
        elif x+y< 2*n+3 and x<n+2 and y<n+2:
            print("#",end="")
        elif y==0 or y==n+1 and x>n+1:
            print("+",end="")
        elif y>0 and y<n+1 and (x==n+2 or x==2*n+3):
            print("+",end="")
        elif y>0 and y<n+1 and x>n+2 and x<2*n+3:
            print("#",end="")
        elif y>n+1 and x<n+2 and (y==n+2 or y==2*n+3):
            print("#",end="")
        elif y>n+1 and x<n+2 and (x==0 or x==n+1):
            print("#",end="")
        elif y>n+1 and x<n+2 and (x>0 or x<n+1):
            print("+",end="")
        elif y>n+1 and x>n+1 and x+y<3*n+6:
            print("+",end="")
        else:
            print(".",end="")
    print()