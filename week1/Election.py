print("*** Election ***")
n = int(input("Enter a number of voter(s) : "))
ans = [0]*20
test = [0]*n
real = 0
for x in range(0,20):
    ans[x] = 0
data = input().split()
for x in range(0,n):
    test[x] = int(data[x])
while n>0:
    n-=1
    if test[n] > 0 and test[n] < 21:
        ans[test[n]-1]+=1
temp = 0     
for x in range(0,20):
    if ans[x] > temp:
        temp = ans[x]
        real = x+1
if real == 0:
    print("*** No Candidate Wins ***")
else:
    print(real)

