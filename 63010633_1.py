print("*** Converting hh.mm.ss to seconds ***")
h,m,s = input("Enter hh mm ss : ").split()
h = int(h)
m = int(m)
s = int(s)
if m > 59 or m < 0:
    print("mm(",end="")
    print(m,end=") is invalid!")
elif s > 59 or s < 0:
    print("ss(",end="")
    print(s,end=") is invalid!")
else:
    ans = h*3600 + m*60 + s
    if h < 10:
        print("0",end="")
        print(h,end=":")
    else:
        print(h,end=":")
    if m < 10:
        print("0",end="")
        print(m,end=":")
    else:
        print(m,end=":")
    if s < 10:
        print("0",end="")
        print(s,end=" = ")
    else:
        print(s,end=" = ")
    print(f"{ans:,d}","seconds")
