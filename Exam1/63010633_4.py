inp = int(input("Enter a positive number : "))
if inp < 1:
    print(inp,'is too low.')
elif inp > 15:
    print(inp,'is too high.')
else:
    for i in range(inp):
        for j in range(inp):
            if i==0:
                print("%X"%(j+1),end=" ")
            elif j==0:
                print("%X"%(i+1),end=" ")
            elif i==inp-1:
                print("%X"%(j),end=" ")
            elif j==inp-1:
                print("%X"%(i),end=" ")
            else:
                print(" ",end=" ")
        print()