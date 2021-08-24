def bon(w):
	### Enter Your Code Here ###
    ans = 0
    for i in range(0,len(w)):
        for j in range(i+1,len(w)):
            if w[i] == w[j]:
                ans = (ord(w[i])-96)*4
    return ans
secretCode = input("Enter secret code : ")
print(bon(secretCode))
