def weirdSubtract(n,k):

	### Enter Your Code Here ###
    temp = n
    while k>0:
        if(temp%10 == 0):
            temp/=10
        else:
            temp-=1
        k-=1
    return int(temp)


n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))
