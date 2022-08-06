print(" *** BMI ***")
x = input("Enter your weight(kg) and height(m) : ").split()
w = int(x[0])
h = float(x[1])
bmi = w/(h*h)
print("Your status is : ",end="")
if bmi < 18.5:
    print("Below normal weight.")
elif bmi < 25:
    print("Normal weight.")
elif bmi < 30:
    print("Overweight.")
elif bmi < 35:
    print("Case I Obesity.")
elif bmi < 40:
    print("Case II Obesity.")
elif bmi >= 40:
    print("Case III Obesity.")