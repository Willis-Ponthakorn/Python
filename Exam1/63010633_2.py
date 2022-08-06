x = int(input("Input : "))
if x<=0:
    print("!!!Please enter number greater than zero!!!")
else:
    print()
    for i in range(x):
        for j in range(2*x):
            if i >= j or i+j>2*x-2:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    for i in range(x-1):
        for j in range(2*x):
            if i+j<=x-2 or j-i>x:
                print("*",end="")
            else:
                print(" ",end="")
        print()