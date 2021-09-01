print(" *** Wind classification ***")
x = float(input("Enter wind speed (km/h) : "))
print("Wind classification is ",end="")
if x < 52:
    print("Breeze.")
elif x < 56:
    print("Depression.")
elif x < 102:
    print("Tropical Storm.")
elif x < 209:
    print("Typhoon.")
else:
    print("Super Typhoon.")
